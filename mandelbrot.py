import math

def round_sig_figs(x, sig_figs):
    if x == 0:
        return 0
    # I don't even wanna know
    digits = sig_figs - int(math.floor(math.log10(abs(x)))) - 1
    return round(x, digits)

# Smaller value goes first
domain_real = [-2, 1]
range_imaginary = [-1.5, 1.5]

resolution = 100
accuracy_sig_figs = 6

iterations = 10

domain_size = abs(domain_real[1] - domain_real[0])
range_size = abs(range_imaginary[1] - range_imaginary[0])

increment = range_size / resolution

real_values = [round_sig_figs(domain_real[0] + increment * n, accuracy_sig_figs) for n in range(round(domain_size / increment) + 1)]
imaginary_values = [round_sig_figs(range_imaginary[0] + increment * n, accuracy_sig_figs) for n in range(round(range_size / increment) + 1)]

def rule(z, c):
    return z ** 2 + c

for real_value in real_values:
    for imaginary_value in imaginary_values:
        c = complex(real_value, imaginary_value)
        z = 0
        behaviour = None
        for i in range(iterations):
            z = rule(z, c)
            if z.real ** 2 + z.imag ** 2 > 4:
                behaviour = False
                break
        if behaviour == None:
            behaviour = True
        print(behaviour)