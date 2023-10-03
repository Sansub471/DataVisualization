import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

size = arr.shape
print(f'The size of the array is {size}')

# Transpose
tpose = arr.transpose()
print(f'The transpose of the matrix is \n {tpose}')
size = tpose.shape
print(f'Size after transpose {size}')

# Linspace

data_cloud = np.linspace(1,10, num= 10,retstep=True, dtype='float64')
print(data_cloud)

# arange

rg = np.arange(15)
print('Arange')
print(type(rg))


# reshape
arr2 = arr.reshape(6,1)
print('Reshape')
print(arr2)


