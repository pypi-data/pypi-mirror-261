import jax
import jax.numpy as jnp
import equinox
from tqdm.auto import tqdm


def base_rejection_sampler(key, target, proposal, n = 1, max_ratio = 1.0):
    """
    Rejection sampler with generic user input proposal distribution.
    There are no python loops, only jax.lax.while_loop - jit not necessary.
    
    Inputs
    ------
    key: jax.random.PRNGKey
        Random seed.
    target: function (shape,) -> ()
        Computes target probability density for a *single* sample.
        Input shape must be that of the random variable, e.g., (2,) for 2D.
        Output shape must be ().
    proposal: function key -> (shape,), ()
        Function that samples and scores a proposal.
        The support of the proposal must contain the support of the target.
        Must take as input a jax.random.PRNGKey.
        Must output a single sample and its probability density.
    n: int
        Number of samples to draw.
    max_ratio: float
        Upper bound > 1 on the density ratio of target / proposal.

    Outputs
    -------
    array (n, *shape)
        Samples drawn from the target density via rejection sampling.
    """
    
    key, ykey = jax.random.split(key)

    y, proposal_y = proposal(ykey)
    assert proposal_y.squeeze().shape == ()
    if proposal_y.shape != ():
        _proposal = proposal
        def proposal(key):
            y, proposal_y = _proposal(key)
            return y, proposal_y.squeeze()
    
    target_y = target(y)
    assert target_y.squeeze().shape == ()
    if target_y.shape != ():
        _target = target
        target = lambda x: _target(x).squeeze()

    shape = y.shape
    dims = tuple(range(1, len(shape) + 1))
    x = jnp.zeros((n, *shape))
    accepted = jnp.zeros((n,)).astype(bool)
    init_val = key, x, accepted

    def cond_fn(val):
        key, x, accepted = val
        return jnp.logical_not(accepted.all())

    def body_fn(val):
        key, x, accepted = val
        key, ukey, *ykeys = jax.random.split(key, 2 + n)
        ykeys = jnp.array(ykeys)
        y, proposal_y = jax.vmap(proposal)(ykeys)
        target_y = jax.vmap(target)(y)
        ratio = target_y / proposal_y
        # max_ratio = max(max_ratio, ratio.max())
        # jax.lax.cond(
        #     jnp.logical_not(jnp.any(ratio > max_ratio)),
        #     lambda: None,
        #     lambda: jax.debug.breakpoint(),
        # )
        u = jax.random.uniform(ukey, (n,), minval = 0.0, maxval = 1.0)
        # this overrides previously accepted samples
        # doesn't matter as this won't reduce efficiency
        accept = u < ratio / max_ratio
        # can prevent override as below, but not necessary:
        # accept = jnp.logical_and(accept, jnp.logical_not(accepted))
        x = jnp.where(jnp.expand_dims(accept, dims), y, x)
        accepted = jnp.logical_or(accept, accepted)
        return key, x, accepted

    key, x, accepted = jax.lax.while_loop(cond_fn, body_fn, init_val)
    
    return x.squeeze()


def rejection_sampler(key, target, lo = 0.0, hi = 1.0, n = 1, max_ratio = 1.0):
    """
    Rejection sampler with uniform proposal distribution.
    There are no python loops, only jax.lax.while_loop - jit not necessary.
    
    Inputs
    ------
    key: jax.random.PRNGKey
        Random seed.
        
    target: function (*shape,) -> ()
        Computes target probability density for a *single* sample.
        Input shape must be that of the random variable, e.g., (2,) for 2D.
        Output shape must be ().
    lo: float | array-like, default = 0.0
        Lower bound for the uniform proposal.
        Must have the same shape as the input to target.
        Scalar value implies target is 1D.
    hi: float | array-like, default = 1.0.
        Upper bound for the uniofrm proposal.
        Must have the same shape as the input to target.
        Scalar value implies target is 1D.
    n: int
        Number of samples to draw.
    max_ratio: None | float
        Upper bound > 1 on the density ratio of target / proposal.
        Default = volume of the uniform proposal.

    Outputs
    -------
    array (n, *shape)
        Samples drawn from the target density via rejection sampling.
    """
    
    lo = jnp.atleast_1d(lo)
    hi = jnp.atleast_1d(hi)
    assert lo.shape == hi.shape
    shape = lo.shape
    proposal_y = 1.0 / jnp.prod(hi - lo)

    def proposal(key):
        y = jax.random.uniform(key, shape, minval = lo, maxval = hi)
        return y, proposal_y

    return base_rejection_sampler(key, target, proposal, n, max_ratio)


def base_rejection_sampler_loop(
    key, target, proposal, n = 1, max_ratio = 1.0, progress = False,
):
    """
    Rejection sampler with generic user input proposal distribution.
    This uses a python loop and jits the proposal iterator.
    
    Inputs
    ------
    key: jax.random.PRNGKey
        Random seed.
    target: function (shape,) -> ()
        Computes target probability density for a *single* sample.
        Input shape must be that of the random variable, e.g., (2,) for 2D.
        Output shape must be ().
    proposal: function key -> (shape,), ()
        Function that samples and scores a proposal.
        The support of the proposal must contain the support of the target.
        Must take as input a jax.random.PRNGKey.
        Must output a single sample and its probability density.
    n: int
        Number of samples to draw.
    max_ratio: float
        Upper bound > 1 on the density ratio of target / proposal.
    progress: bool, default = False
        Display a progress bar.

    Outputs
    -------
    array (n, *shape)
        Samples drawn from the target density via rejection sampling.
    """
    
    key, ykey = jax.random.split(key)

    y, proposal_y = proposal(ykey)
    assert proposal_y.squeeze().shape == ()
    if proposal_y.shape != ():
        _proposal = proposal
        def proposal(key):
            y, proposal_y = _proposal(key)
            return y, proposal_y.squeeze()
    
    target_y = target(y)
    assert target_y.squeeze().shape == ()
    if target_y.shape != ():
        _target = target
        target = lambda x: _target(x).squeeze()

    shape = y.shape
    dims = tuple(range(1, len(shape) + 1))
    x = jnp.zeros((n, *shape))
    accepted = jnp.zeros((n,)).astype(bool)
    init_val = key, x, accepted

    @equinox.filter_jit()
    def step(key, x, accepted):
        key, ukey, *ykeys = jax.random.split(key, 2 + n)
        ykeys = jnp.array(ykeys)
        y, proposal_y = jax.vmap(proposal)(ykeys)
        target_y = jax.vmap(target)(y)
        ratio = target_y / proposal_y
        # max_ratio = max(max_ratio, ratio.max())
        # assert jnp.logical_not(jnp.any(ratio > max_ratio))
        u = jax.random.uniform(ukey, (n,), minval = 0.0, maxval = 1.0)
        accept = u < ratio / max_ratio
        accept = jnp.logical_and(accept, jnp.logical_not(accepted))
        x = jnp.where(jnp.expand_dims(accept, dims), y, x)
        accepted = jnp.logical_or(accept, accepted)
        return key, x, accepted

    if progress:
        naccepted = accepted.sum()
        pbar = tqdm(total = n)

    while jnp.logical_not(accepted.all()):
        key, x, accepted = step(key, x, accepted)

        if progress:
            pbar.update(int(accepted.sum() - naccepted))
            naccepted = accepted.sum()

    if progress:
        pbar.close()
    
    return x.squeeze()


def rejection_sampler_loop(
    key,
    target,
    lo = 0.0,
    hi = 1.0,
    n = 1,
    max_ratio = 1.0,
    progress = False,
):
    """
    Rejection sampler with uniform proposal distribution.
    This uses a python loop and jits the proposal iterator.
    
    Inputs
    ------
    key: jax.random.PRNGKey
        Random seed.
        
    target: function (*shape,) -> ()
        Computes target probability density for a *single* sample.
        Input shape must be that of the random variable, e.g., (2,) for 2D.
        Output shape must be ().
    lo: float | array-like, default = 0.0
        Lower bound for the uniform proposal.
        Must have the same shape as the input to target.
        Scalar value implies target is 1D.
    hi: float | array-like, default = 1.0.
        Upper bound for the uniofrm proposal.
        Must have the same shape as the input to target.
        Scalar value implies target is 1D.
    n: int
        Number of samples to draw.
    max_ratio: float
        Upper bound > 1 on the density ratio of target / proposal.
    progress: bool, default = False
        Display a progress bar.

    Outputs
    -------
    array (n, *shape)
        Samples drawn from the target density via rejection sampling.
    """
    
    lo = jnp.atleast_1d(lo)
    hi = jnp.atleast_1d(hi)
    assert lo.shape == hi.shape
    shape = lo.shape
    proposal_y = 1.0 / jnp.prod(hi - lo)

    def proposal(key):
        y = jax.random.uniform(key, shape, minval = lo, maxval = hi)
        return y, proposal_y

    return base_rejection_sampler_loop(
        key, target, proposal, n, max_ratio, progress,
    )
