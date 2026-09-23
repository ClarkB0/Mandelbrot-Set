import math
from PIL import Image

def round_sig_figs(x, sig_figs):
    if x == 0:
        return 0
    # I don't even wanna know
    digits = sig_figs - int(math.floor(math.log10(abs(x)))) - 1
    return round(x, digits)


def generate_points(domain_real, range_imaginary, resolution, accuracy_sig_figs=6):
    domain_size = abs(domain_real[1] - domain_real[0])
    range_size = abs(range_imaginary[1] - range_imaginary[0])

    increment = range_size / resolution
    x_points = round(domain_size / increment) + 1
    y_points = round(range_size / increment) + 1

    real_values = [round_sig_figs(domain_real[0] + increment * n, accuracy_sig_figs) for n in range(x_points)]
    imaginary_values = [round_sig_figs(range_imaginary[0] + increment * n, accuracy_sig_figs) for n in range(y_points)]
    return real_values, imaginary_values


def rule(z, c):
    return z ** 2 + c


def check_bound(z, c, iterations):
    for _ in range(iterations):
        z = rule(z, c)
        if z.real ** 2 + z.imag ** 2 >= 4:
            return False
    return True


def draw_mandelbrot_set(real_values, imaginary_values, iterations):
    bound_points = []
    for x in range(len(real_values)):
        for y in range(len(imaginary_values)):
            c = complex(real_values[x], imaginary_values[y])
            z = 0
            if check_bound(z, c, iterations):
                bound_points.append([x, y])

    img = Image.new("RGB", (len(real_values), len(imaginary_values)), "white")
    pixels = img.load()

    for point in bound_points:
        pixels[point[0], point[1]] = 0

    img.save("mandelbrot.png")
    img.show()


if __name__ == '__main__':
    # Smaller value goes first
    domain_real = [-2, 1]
    range_imaginary = [-1.5, 1.5]

    resolution = 255
    accuracy_sig_figs = 6

    iterations = 500

    real_values, imaginary_values = generate_points(domain_real, range_imaginary, resolution, accuracy_sig_figs)
    draw_mandelbrot_set(real_values, imaginary_values, iterations)