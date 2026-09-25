import numpy as np

domain_real = [-2.0, 1]
range_imaginary = [-1.5, 1.5]

resolution = 1000

resolution_x = resolution
increment = abs(domain_real[0] - domain_real[1]) / resolution
resolution_y = int(abs(range_imaginary[0] - range_imaginary[1]) / increment)

real_values = np.linspace(domain_real[0], domain_real[1], num=resolution_x)
imaginary_values = np.linspace(range_imaginary[0], range_imaginary[1], num=resolution_y)

# meshgrid returns arrays for each possible real value for each possible imaginary value
# in the each column is each possible real value, with a row for each possible imaginary value
# 
real, imaginary = np.meshgrid(real_values, imaginary_values)

print(real_values)