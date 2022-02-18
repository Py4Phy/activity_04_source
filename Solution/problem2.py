# Problem 2

import numpy as np
positions = np.array(
    [[0.0, 0.0, 0.0], [1.34234, 1.34234, 0.0],
     [1.34234, 0.0,  1.34234], [0.0, 1.34234, 1.34234]])
t = np.array([1.34234, -1.34234, -1.34234])

positions2 = np.array([[1.5, -1.5, 3], [-1.5, -1.5, -3]])
t2 = np.array([-1.5, 1.5, 3])

# replace NotImplemented with your solution

# (a) shape and dimension of positions
result2a_shape = positions.shape
result2a_dimensions = positions.ndim

print(f"2a shape of positions:      {result2a_shape}")
print(f"2a dimensions of positions: {result2a_dimensions}")


# (b) shape and dimension of t
result2b_shape = t.shape
result2b_dimensions = t.ndim

print(f"2b shape of t:      {result2b_shape}")
print(f"2b dimensions of t: {result2b_dimensions}")


# (c)
result2c = positions[1]


# (d) (i)
result2d = positions[1, 1]


# (e)
result2e = positions[:, 1]

result2e_shape = result2e.shape
result2e_dimensions = result2e.ndim

print(f"2e all y:               {result2e}")
print(f"2e shape of all y:      {result2e_shape}")
print(f"2e dimensions of all y: {result2e_dimensions}")

# (f)
result2f = positions + t

# (g)
# add your function definition here
def translate(coordinates, t):
    """translate coordinates (Nx3) by vector t (3x1)"""
    return coordinates + t
