# 2-D

import numpy as np


arr = np.array([[12, 23, 34, 46], [32, 43, 54, 56], [67,89, 69, 90]])

# print(arr)

# print(np.ndim(arr))

# print(arr[1, 2])  # 54 should be printed

# 3-D

arr3 = np.array([[[12, 23, 34], [232, 12, 332]],
        [[12, 32, 11], [121, 323, 123] ]])

print(arr3)

# print(np.ndim(arr3))

print(arr3[1, 1, 0])


