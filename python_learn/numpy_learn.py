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

# arr.flatten()

arr = np.array([[1,2,3], [4,5,6]])

flattened_array = arr.flatten()
print(flattened_array)

# np.ravel() : creates 1d array out of the same nd array

arr = np.array([[1,2,3], [4,5,6]])

arr = np.ravel(arr)
print(arr)

# np.transpose()


arr_2d = np.array([[1,2,3], [4,5,6]])
transpose = np.transpose(arr_2d)



print(transpose)

# arr.T : returns the transpose

arr_2d = np.array([[1,2,3],[4,5,6]])

print(arr_2d.T)

# np.concatenate()

arr1 = np.arange(1,5).reshape(2,2)
arr2 = np.arange(5,9).reshape(2,2)

a = np.concatenate((arr1, arr2), axis=0)
b = np.concatenate((arr1, arr2), axis=1)
print(a, b, sep='\n')


#     iteration


arr = np.arange(1, 10).reshape((3,3))

rows, cols = arr.shape


for i in range(rows) : 
    for j in range(cols) : 
        print(arr[i][j], end = ' ')
    print()

for i in arr.flat :
    print(i)
    
    
# vectorized operations : 

arr1 = np.arange(1, 5)
arr2 = np.arange(5, 9)

arr = arr1 + arr2
print(arr)   

# update ndarray in place

arr = np.arange(1, 6)

with np.nditer(arr, flags=['buffered'], op_flags=['readwrite']) as it : 
    
    for x in it : 
        x[...] =  x * 2

print(arr)


#    slicing 

arr = np.arange(9).reshape((3,3))

print(arr)
print(arr[..., 1:])


arr = np.arange(10)

print(arr[arr > 5])

# find all complex number

a = np.array( [1, 2 + 6j ,5, 3.5 + 5j]  )

print(a[ np.iscomplex(a) ])

# array size

a = np.arange(10)
print(len(a), a.size)


# operations

a = np.array([10,20, 30])
b = np.array([1,2,3])

print(a / b)

a = np.arange(4)
print(np.power(a, 2))

scalar= 10
print(a + 10)

#                   date  and time arrays

start_date = np.datetime64('2024-08-01')
end_date = np.datetime64('2024-08-10') 


gap = end_date - start_date

arr = np.linspace(0, gap.astype(np.int64), 5).astype(np.int64)
print(start_date + arr)
