import random

def rand():

    return random.random()

def randint(a, b):

    return random.randint(int(a), int(b))

def randfloat(a, b):

    return random.uniform(a, b)

def choice(items):

    if not isinstance(items, list) or len(items) == 0:
        raise ValueError("choice() requires a non-empty list")
    return random.choice(items)

def shuffle_list(items):

    if not isinstance(items, list):
        raise ValueError("shuffle() requires a list")
    shuffled = items.copy()
    random.shuffle(shuffled)
    return shuffled

def sample(items, k):

    if not isinstance(items, list):
        raise ValueError("sample() requires a list")
    return random.sample(items, int(k))

def seed(value):

    random.seed(int(value))
    return f"Random seed set to {int(value)}"


RANDOM_FUNCTIONS = {
    'rand': rand,
    'random': rand,  
    'randint': randint,
    'randfloat': randfloat,
    'choice': choice,
    'shuffle': shuffle_list,
    'sample': sample,
    'seed': seed,
}

def get_function(name):
    if name in RANDOM_FUNCTIONS:
        return RANDOM_FUNCTIONS[name]
    else:
        raise ValueError(f"Unknown random function: {name}")