
#1. Importing matplotlib:
import matplotlib.pyplot as plt

#2. Creating a simple line plot:
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()


"""This creates a simple sine wave plot."""

#3. Adding labels and title:
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')
plt.show()


#4. Multiple plots on the same figure:
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.legend()
plt.show()


#5. Scatter plot:
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.show()

#6. Histogram:
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()


#7. Subplots:
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, np.sin(x))
ax2.plot(x, np.cos(x))
plt.show()


#8. Customizing plot appearance:
plt.plot(x, np.sin(x), color='red', linestyle='--', linewidth=2, marker='o')
plt.show()


#9. Saving a plot:
plt.plot(x, np.sin(x))
plt.savefig('sine_wave.png')