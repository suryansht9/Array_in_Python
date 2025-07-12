import numpy as np

# Simulate 1000 dice rolls
rolls = np.random.randint(1, 7, size=1000)

# Count the frequency of each face (1 through 6)
counts = np.bincount(rolls)[1:]  # skip index 0

# Display the results
for face, count in enumerate(counts, start=1):
    print(f"Face {face}: {count} times")

# Optional: Display as a bar chart
try:
    import matplotlib.pyplot as plt
    plt.bar(range(1, 7), counts, color='skyblue')
    plt.title("Frequency of Dice Rolls (1000 Rolls)")
    plt.xlabel("Dice Face")
    plt.ylabel("Count")
    plt.grid(True)
    plt.show()
except ImportError:
    print("matplotlib not installed. Skipping chart.")
