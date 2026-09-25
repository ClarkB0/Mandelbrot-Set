import numpy as np

def generate_mandelbrot(width, height, max_iter):
    # 1. Create the complex grid (c)
    x = np.linspace(-2.0, 0.5, width)
    y = np.linspace(-1.25, 1.25, height)
    real, imag = np.meshgrid(x, y)
    c = real + 1j * imag
    
    # 2. Initialize tracking arrays
    z = np.zeros_like(c)
    output = np.zeros(c.shape, dtype=int)  # Stores the iteration count when it escaped
    still_inside = np.ones(c.shape, dtype=bool)  # Tracks active points

    # 3. Iteratively apply the rule and check bounds
    for i in range(max_iter):
        # Only update points that haven't escaped yet
        z[still_inside] = z[still_inside]**2 + c[still_inside]
        
        # Performance trick: calculate squared magnitude to avoid square roots
        escaped_this_turn = (z.real**2 + z.imag**2) > 4
        
        # Find points that JUST escaped on this exact iteration
        newly_escaped = escaped_this_turn & still_inside
        output[newly_escaped] = i
        
        # Update our mask for the next iteration
        still_inside &= ~escaped_this_turn
        
        # Optional: Stop early if every single point has escaped
        if not np.any(still_inside):
            break
            
    return output