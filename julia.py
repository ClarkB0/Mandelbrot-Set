import math
from PIL import Image

def round_sig_figs(x: float, sig_figs: int):
    if x == 0:
        return 0
    # I don't even wanna know
    digits = sig_figs - int(math.floor(math.log10(abs(x)))) - 1
    return round(x, digits)


def generate_points(domain_real: list, range_imaginary: list, resolution: int, accuracy_sig_figs: int = 6):
    domain_size = abs(domain_real[1] - domain_real[0])
    range_size = abs(range_imaginary[1] - range_imaginary[0])

    increment = range_size / resolution
    x_points = round(domain_size / increment) + 1
    y_points = round(range_size / increment) + 1

    real_values = [round_sig_figs(domain_real[0] + increment * n, accuracy_sig_figs) for n in range(x_points)]
    imaginary_values = [round_sig_figs(range_imaginary[0] + increment * n, accuracy_sig_figs) for n in range(y_points)]
    return real_values, imaginary_values


def check_bound(z: complex, c: complex, iterations: int):
    rule = lambda z, c: z ** 2 + c

    for _ in range(iterations):
        z = rule(z, c)
        if abs(z) > 2:
            return False
    return True


def draw_mandelbrot_set(real_values: list, imaginary_values: list, c: complex, iterations: int):
    bound_points = []
    for x in range(len(real_values)):
        for y in range(len(imaginary_values)):
            z = complex(real_values[x], imaginary_values[y])
            if check_bound(z, c, iterations):
                bound_points.append([x, y])

    img = Image.new("RGB", (len(real_values), len(imaginary_values)), "white")
    pixels = img.load()
    assert pixels is not None, "Image creation failed."

    for point in bound_points:
        pixels[point[0], point[1]] = 0

    img.save("julia.png")
    img.show()


if __name__ == '__main__':
    # Smaller value goes first
    domain_real = [-1, 1]
    range_imaginary = [-1, 1]
    c = -0.5125 + 0.5213j

    # Number of points (imaginary axis)
    # From 0 to resolution (inclusive)
    # The the increment of the real axis is set to the same as the imaginary axis
    resolution = 1000
    accuracy_sig_figs = 6

    # Maximum iterations to check whether the C value results in bound/escaping behaviour
    # A higher number more accurately represents the Mandelbrot set
    iterations = 100

    real_values, imaginary_values = generate_points(domain_real, range_imaginary, resolution, accuracy_sig_figs)
    draw_mandelbrot_set(real_values, imaginary_values, c, iterations)