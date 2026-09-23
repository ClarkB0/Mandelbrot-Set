import math, csv
from PIL import Image

def round_sig_figs(x, sig_figs):
    if x == 0:
        return 0
    # I don't even wanna know
    digits = sig_figs - int(math.floor(math.log10(abs(x)))) - 1
    return round(x, digits)


# Smaller value goes first
domain_real = [-2, 1]
range_imaginary = [-1.5, 1.5]

resolution = 1000
accuracy_sig_figs = 6

iterations = 1000

domain_size = abs(domain_real[1] - domain_real[0])
range_size = abs(range_imaginary[1] - range_imaginary[0])

increment = range_size / resolution
points_x = round(domain_size / increment) + 1
points_y = round(range_size / increment) + 1

real_values = [round_sig_figs(domain_real[0] + increment * n, accuracy_sig_figs) for n in range(points_x)]
imaginary_values = [round_sig_figs(range_imaginary[0] + increment * n, accuracy_sig_figs) for n in range(points_y)]


def rule(z, c):
    return z ** 2 + c


def check_bound(z, c, iterations):
    for _ in range(iterations):
        z = rule(z, c)
        if z.real ** 2 + z.imag ** 2 >= 4:
            return False
    return True


bound = []
for x in range(points_x):
    for y in range(points_y):
        c = complex(real_values[x], imaginary_values[y])
        z = 0
        if check_bound(z, c, iterations):
            bound.append([x, y])

img = Image.new("RGB", (points_x, points_y), "white")
pixels = img.load()

for point in bound:
    pixels[point[0], point[1]] = 0

img.save("mandelbrot.png")
img.show()