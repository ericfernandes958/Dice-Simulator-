import numpy as np

rng = np.random.default_rng()
numbers = np.array([1, 2, 3, 4, 5, 6])

data = rng.choice(numbers, 10000)
