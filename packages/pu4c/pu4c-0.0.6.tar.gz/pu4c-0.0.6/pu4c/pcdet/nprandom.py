import numpy as np

rand_seed = None
def seed(seed):
    global rand_seed
    rand_seed = seed

def rand(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.rand(*args, **kwargs)
def randint(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.randint(*args, **kwargs)
def randn(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.randn(*args, **kwargs)
def random(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.random(*args, **kwargs)
def choice(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.choice(*args, **kwargs)
def uniform(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.uniform(*args, **kwargs)
def normal(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.normal(*args, **kwargs)
def shuffle(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.shuffle(*args, **kwargs)
def sample(*args, **kwargs):
    if rand_seed is not None: np.random.seed(rand_seed)
    return np.random.sample(*args, **kwargs)