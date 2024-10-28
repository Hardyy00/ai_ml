from functools import wraps

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

# set operations : 

# 1. union

a = {'a', 'b', 'c'}
b = { 'a', 'd'}

print(a | b)

print(a.union(b))

# intersection 
print(a & b)

#  set difference

print(a - b)

# set symmertric difference

print(a ^ b)


# frozenset  : immutable set

s = frozenset({1,3,34,34,32})

print(s , type(s))


# dictionary

dic = { 'name' : 'hardik', 'age' : 21, 'job' : "dev"}

print(dic , type(dic))

ls = [ ('name', 'bob'),('age', 21)]


d = dict(ls)

print(d)


# ways to create a dict

keys = [1, 2 , 3, 4]
values = [5,6,7,8]

d = dict(zip(keys, values))
print(d)


# keys with a default values

keys = ['a', 'b', 'c']
defaultValue = 0

d = dict.fromkeys(keys, defaultValue)
print(d)


# access from a dict

d = { 'name' : 'hardik', 'age' : 21, 'job' : "dev"}

print(d['name'])

print(d.get('name'))


d['city'] = 'agra'

print(d)


# remove an item
d.pop("city")
print(d)

del d['job']

print(d)


# keys(), values(), items()

D = {'name': 'Bob',
     'age': 25,
     'job': 'Dev'}


print(list(D.keys()))

print(list(D.values()))

print(list(D.items()))


# dictionary comprehension

d = { x  : x**2 for x in range(5)}

print(d)
d = {x : x*3  for x in 'abc'}

print(d)

# creating a subset of a dictionary

D = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

selectedKeys = [0,2,5]

d = { key : D[key] for key in selectedKeys}
print(d)

# reverse a dict

d = {v : k for k, v in D.items()}

print(d)


# enumerate()

L = ['red', 'green', 'blue']

d = {k : v for k, v in enumerate(L)}

print(d)


keys = ['name', 'age', 'job']
values = ['Bob', 25, 'Dev']


D = {k : v for k, v in zip(keys, values)}

print(D)

print(dict(zip(keys, values)))


#       strings


s = """Hi
Hardik Gaur"""

print(s)

# type conversion

s = str(42)

print(s)

s = "hardikgaur"

print(s[:], s[1:], s[0:-1] , s[::-1])


# implicit concatenation 

s = "Hello" " World"

print(s)

s = ('hardik'
     ' gaur' ' is a good boy')

print(s)

print('-' * 10)

print(len(s))


s = "Hello World"

s2 = s.replace("World", 'Hardik')

print(s, s2)


s = 'red,green,blue,yellow'
s = s.split(',')
s = '|'.join(s)

print(s)

# every word first letter capital : title()

S = 'hello, world!'

print(S.title())

# f strings

name = 'Hardik'

s = f"hii {name}"
print(s)


# conditional statement

x , y = 2,1
print("yes") if x > y else print("no")


# while loop

x = 1

while x<4 : 
    print(x)
    x +=1

l = [1, 2, 3]

while l : 
    print(l.pop())



# functions

def hello() :
    print("Hii")

hello()   

def foo(name, age):
    print(name, ' is at ', age)

foo(name='Hardik', age=21)  

def foo(name, age , job='dev') : 
    print(name , ' is at ', age, ' and is a ', job)

foo(name ='Hardik',age= 21)

def closure(a, b):

    def sum() : 
        return a + b
    
    return sum()

print(closure(1,2))

# lambda functions


L = [('Sam', 35),
    ('Max', 25),
    ('Bob', 30)]


x = sorted(L, key=lambda x : x[1])

print(x)


#                                                       decorator

# manual way

# def decorator(func) : 
#     def wrapper() : 
#         print("Calling the function")
#         func()
#         print("Finished")
#     return wrapper


# def hello() :
#     print("Hello")

# hello = decorator(hello)
# hello()


# syntactic sugar


# def decorator(func) : 

#     def wrapper() : 

#         print("Calling")
#         func()
#         print("finished")
#     return wrapper

# @decorator  # add the decorator name
# def hello() : 
#     print("Hello world")


# hello()



# passing arguments

# def decorator(func) : 
    
#     def wrapper(*args ,**kwargs) : 
#         print("Calling")
#         func(*args, **kwargs)
#         print("finished")
#     return wrapper

# @decorator
# def hello(name) : 
#     print("Hello " + name)


# hello("Hardik")


# returning a value

# def decorator(func) : 

#     def wrapper(*args, **kwargs) : 
#         print("Calling")
#         result = func(*args, **kwargs)
#         print("Finished")
#         return result  
#     return wrapper

# @decorator
# def hello(name) : 
#     return "Hello " + name

# print(hello("hardik"))


# preseving function's metadata like name, docstring etc.


# def hello(name) : 
#     """prints hello 'name'"""
#     print("Hello " + name)

# print(hello.__name__)
# print(hello.__doc__)




# to preserve metadata above the wrapper function , use @wrap(func) ( this is imported from functool )
def decorat(func) : 
    
    @wraps(func)
    def wrapper(*args ,**kwargs) : 
        print("Calling")
        func(*args, **kwargs)
        print("finished")
    return wrapper

@decorat
def hello(name) : 
    """prints hello 'name'"""
    print("Hello " + name)

print(hello.__name__)
print(hello.__doc__)

#  unwrapping a decorator


original = hello.__wrapped__

original("Hardik")






