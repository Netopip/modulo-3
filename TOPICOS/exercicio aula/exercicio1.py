import numpy as np


array = np.random.randint(10, size=(5,))
print(array)
print(array * 2)
print(array ** 2)
print(array - 1)
print(array + 10)
print(array < 5)

array_1 = np.random.randint(10, size=(7,))
array_2 = np.random.randint(10,size=(7,))

print(array_1)
print(array_2)

print(array_1 + array_2)
print(array_1 * array_2)


array_3 = np.random.randint(10, size=(7,))
print('array 3')
print(array_3)
print(np.mean(array_3))
print(np.median(array_3))
print(np.max(array_3))
print(np.min(array_3))

