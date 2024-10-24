# complex number

x = 3 + 4j

print(x.real, x.imag)


# list

ls = [1,2,3,4]
print(ls)

ls = list('abc')
print(ls)

# using -ve index

ls = [1,2,3,4,5,6,7]

# print(ls[-1])


# slicing a list

ls = ['a', 'b', 'c', 'd', 'e', 'f']

print(ls[2:5])

print(ls[3:-1])


print(ls[0::2])  # start : end+1 : step

ls.append('g')


# ls.extend(['h', 'i', 'j'])

ls += ['h', 'i']

print(ls)


# remove from list 

ls.pop()  # remove from last
print(ls)


ls.pop(0)

print(ls)


# using del statement

del ls[0]

print(ls)


# delete by value (not by index)

ls.remove('e')

print(ls)

# del a large part

del ls[0:2]

print(ls)

# clear a list

ls.clear()

# list replication

l = [1]

l *=3

print(l)

# list length

print(len(l))


# check if item exists or not

print( 1 in l )

print( 1 not in l)


# iterate through a list

ls = ['a', 'b', 'c', 'd', 'e']

for i in ls : 
    print(i)


# using range()


for i in range(len(ls)) : 
    print(ls[i])


# using enumerate : 

for index, value in enumerate(ls) : 
    print(index , value, sep=' ',end='\n')   


# slicing using -ve indices

print(ls[-5 : -2])    


# reversing the lst


print(ls[::-1])



# insert multiple elements at the beginning

ls = ['a', 'b', 'c']


ls[:0] = ['x', 'y', 'z']

print(ls)

# creating a copy of a list


ls2 = ls[:]

print(ls2)


# list comprehension

# squares of integers from 0 to 4

ls = [x ** 2 for x in range(5)]


# apply abs 

ls = [-2,3,-8,-9,-10]

ls = [ abs(i) for i in ls]

print(ls)

# using if , iterable's items are skipped for which the clause is not true

ls = [-4, 4,3,-9]

ls = [ x for x in ls if x>=0]

print(ls)


# using nested list comprehension


ls = [[1,2,3], [4,5,6], [7,8,9]]

ls = [x for l in ls for x in l]
print(ls)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]



# transpose the matrix

ls = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(ls)

# applying map

# collecting ascii value of each character

ls = list(map(ord, 'abc'))  # in the case of already-defined functions, map is faster than list comperhension
print(ls)

# list of squares

ls = list( map( lambda x : x**2 , range(5) ) )  # in case of user defined function list comprehension is faster then map

print(ls)



# filter() 

ls = list(range(10))


ls = [ x for x in ls if x % 2 == 0]

print(ls)

ls = list( filter(  lambda x : x %2 == 0, ls  ) )

print(ls)


# Tuples

tup = (1,2,3,4,'hardik')

print(tup)

tup = ()   # empty tuple

print(tup)

# singleton tuple

tup = (1,)
print(tup, type(tup))


# tuple unpacking

tup = ('a', 'b', 'c', 'd')

(a, b ,c,d) = tup

print(a, b ,c ,d)

# swapping two variables

a = 1
b = 2

a , b = b, a
print(a, b)

# while unpacking , the right side can  be any kind of sequence (tuple, string or list)

addr = 'hardik@gmail.com'
a, b = addr.split("@")
print(a, b)

# tuple can be joined

tup = (1,2,3) + (4,5,6)
print(tup)

# two method to sort a tuple

tup = ('cc', 'aa', 'dd', 'bb')
print(tuple(sorted(tup)))


tmp = list(tup)
tmp.sort()
tup = tuple(tmp)

print(tup)


# set


# set = {'red', 'green', 'blue'}

# print(set)


print(set([1,2,3]))

st = {1,2,3}

st.add("hardik")
print(st)

print('hardik' in st)


# add multiple items to a set using update()

st.update([4,5,6])
print(st)

