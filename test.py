import numpy as np

features = np.array(
    [
        [-1, -1],
        [-1, 1],
        [1, -1],
        [1, 1]
    ])
print(features)

a = np.array([1,2,5], dtype='int32') # specify data type; int16, int8, int32
print(a)


ran = np.random.rand(4,2)
#ransample = np.random.random_sample(a.shape)
print(f'Random numbers between 0 and 1 \n{ran}')
#print(f'Random Sample like a \n{ransample}')

ranint = np.random.randn(-0.5,0.5, size=(2,2))
print(ranint)

