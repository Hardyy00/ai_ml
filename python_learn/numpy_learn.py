import numpy as np


arr = np.array([[1,2,3], [4,5,6]])
print(arr)

print(arr.shape)

d = np.dtype([('age', np.int64)])

arr = np.array([(1,), (2,), (3,)], dtype=d)

print(arr['age'])

# np.zeros()
arr = np.zeros(5,dtype=np.int64)
print(arr)

# np.ones()
arr = np.ones((2,3))

print(arr)


# np.arrange()

arr = np.arange(1, 11, 2) # end is exclusive
print(arr)

arr = np.linspace(1, 20, 9) # end is inclusive
print(arr)


# creating an empty array

arr = np.empty((2,3))

print(arr)

# creating array of same values

arr = np.full((3,3), 10)
print(arr)



#           array manipulation 

# reshape
arr = np.reshape(np.arange(9), (3,-1))  # -1 infers the other value 

print(arr)

# .flat() : gives us an iterator in for of 1d-array

arr = np.full((3,3),10)

for i in arr.flat : 
    print(i, end=' ')
print()