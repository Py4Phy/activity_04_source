# Problem 1

import numpy as np

sx = np.array([[0, 1], [1, 0]])
sy = np.array([[0, -1j],[1j, 0]])
sz = np.array([[1, 0], [0, -1]])

# replace NotImplemented with your solution

# a
result1a = sx * sy * sz

print(f'1a sx * sy * sz = {result1a}\n')

# b
result1b = sx.dot(sy).dot(sz)

# or
# result1b = sx @ sy @ sz

print(f'1b sx @ sy @ sz = {result1b}\n')

# c
result1c = sx.dot(sy) - sy.dot(sx)

print(f'1c [sx, sy] = {result1c}\n')

# d
v = np.array([1, -1j]) / np.sqrt(2)
result1d = v.conjugate().T.dot(sy.dot(v))

print(f"1d v = {v}")
print(f"1d <v|sy|v> = {result1d}\n")

