import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
numbers = np.array([1, 2, 3, 4, 5, 6])

rolls = rng.choice(numbers, 10000)

colours = ["red", "blue", "green", "purple", "pink", "orange"]

frequency = np.bincount(rolls)[1:]

plt.pie(frequency, labels=numbers, autopct="%1.1f%%", colors=colours)

plt.title("Dice roll distribution")

plt.show()
