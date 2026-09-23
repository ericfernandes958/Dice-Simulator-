import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import RadioButtons

rng = np.random.default_rng()

numbers = np.arange(1, 7)
sample_sizes = [10, 100, 1_000, 10_000, 100_000]

# Generation

results = {}
colours = ["red", "blue", "green", "purple", "pink", "orange"]

# Results for pie and grouped bar chart

for size in sample_sizes:
    rolls = rng.choice(numbers, size)
    frequency = np.bincount(rolls, minlength=7)[1:]
    results[size] = frequency

# Error calculations

errors = {}

for size in sample_sizes:
    frequency = results[size]

    actual_Percetage = (frequency / size) * 100
    expected_Percentage = 100 / 6
    percentage_Error = np.abs(actual_Percetage - expected_Percentage)

    errors[size] = np.mean(percentage_Error)


figure, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))


def update_graph(sample_size):
    frequency = results[sample_size]
    expected = sample_size / 6

    # Clear screen

    ax1.clear()
    ax2.clear()

    # Pie chart

    ax1.pie(frequency, labels=numbers, autopct="%1.1f%%", colors=colours)
    ax1.set_title(f"Dice Roll Distribution ({sample_size:,} rolls)")

    width = 0.4

    # Bar graph

    ax2.barh(numbers - width / 2, [expected] * 6, height=width, label="Expected")
    ax2.barh(numbers + width / 2, frequency, height=width, label="Actual")

    ax2.set_title(f"Expected vs Actual ({sample_size:,} rolls)")
    ax2.set_xlabel("Frequency")
    ax2.set_ylabel("Dice face")
    ax2.legend()

    figure.canvas.draw_idle()


# Radio buttons

radio_ax = figure.add_axes([0.02, 0.3, 0.12, 0.4])
radio = RadioButtons(radio_ax, [str(size) for size in sample_sizes])
radio.on_clicked(lambda label: update_graph(int(label)))

ax3.plot(sample_sizes, [errors[size] for size in sample_sizes], marker="o")

ax3.set_title("How does Sample Size affect Average Error?")
ax3.set_xlabel("No of rolls")
ax3.set_ylabel("Average Percentage error")
ax3.set_xscale("log")
ax3.grid(True)


# Initial graph

update_graph(10_000)

plt.show()
