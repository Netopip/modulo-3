
import numpy as np


array = np.array([[1,2,3],[4,5,6]])
print(array)
print(array.ndim)#numero de dimensões
print(array.shape)#linhas/colunas
print(array[1,2])#segudno dimensao 3 elemento
print(array.dtype)



array[1,0] = 43
print(array)
print()
novo_array = np.zeros((3,3))
novo_array[2,2] = 3
print(novo_array)
print()

novo_array_1 = np.ones((3,3))
print(novo_array_1)

novo_array_2 = np.random.random((2,2))
print(novo_array_2)

novo_array_3 = np.random.randint(20,size=(2,2))
print(novo_array_3)

novo_array_4 = np.arange(5)
print(novo_array_4)



