import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x, y1, label='Sine Wave', color='blue', linewidth=2)
plt.plot(x, y2, label='Cosine Wave', color='orange', linewidth=2)

# Customize (Every element must be added manually)
plt.title('Matplotlib Static Output Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True)

# Display flat image
plt.show()
