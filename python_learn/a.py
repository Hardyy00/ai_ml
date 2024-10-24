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


