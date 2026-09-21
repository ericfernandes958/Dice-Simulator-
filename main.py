import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
numbers = np.array([1, 2, 3, 4, 5, 6])

rollNo = 10000

rolls = rng.choice(numbers, rollNo)

# Lists displaying data to be presented

colours = ["red", "blue", "green", "purple", "pink", "orange"]
frequency = np.bincount(rolls)[1:]
expected = [rollNo / 6] * 6

# Creates a figure with two graphs on one page

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Pie chart

ax1.pie(frequency, labels=numbers, autopct="%1.1f%%", colors=colours)
ax1.set_title("Dice Roll Distribution")

# Grouped bar chart

width = 0.4

ax2.barh(numbers - width / 2, expected, height=width, label="Expected")
ax2.barh(numbers + width / 2, frequency, height=width, label="Actual")

ax2.set_title("Expected vs Actual")
ax2.set_xlabel("Frequency")
ax2.set_ylabel("Dice face")

ax2.legend()
plt.tight_layout()


plt.show()
