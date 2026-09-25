import numpy as np

x_values = np.linspace(0, 9, num=10)
y_values = np.linspace(6, 10, num=5)

x, y = np.meshgrid(x_values, y_values)
# Returns a tupe of arrays of big vectors

print(x)
print(y)