# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:20:34 2021

@author: sartaj
"""

import numpy as np

my_list = [1,2,3,4]
print(my_list)
print(type(my_list))

my_list_np = np.array(my_list)
print(my_list_np)
print(type(my_list_np))
print(my_list_np.shape)
print(my_list_np.ndim)

my_list1 = [[1,2,3],[4,5,6],[7,8,9]]
print(my_list1)
print(type(my_list1))

my_list1_np = np.array(my_list1)
print(my_list1_np)
print(type(my_list1_np))
print(my_list1_np.shape)
print(my_list1_np.ndim)


x = np.arange(1,11) ##Important
print(x)
print(type(x))


y = np.zeros(6)
print(y)
print(type(y))


z = np.zeros((3,3))
print(z)
print(type(z))


j = np.linspace(1,10,10)
print(j)
print(type(j))


r = np.random.rand(3,3)
print(r)
print(type(r))


rn = np.random.randn(3,3)
print(rn)
print(type(rn))


rin = np.random.randint(1,101,20)
print(rin)

rin2 = np.random.randint(10, size=5)
print(rin2)

rin3 = np.random.randint(1,10,size=(4,5))
print(rin3)

#Max / Min val of an array:
print(rn.max())
print(rn.min())


#Max / Min val's idx of an array:
print(j.argmax())
print(j.argmin())


k = np.arange(1,100,5)
print(k)

k = k.reshape(5,4) # (row,column)
print(k)


#Append:-

l = np.arange(1,10,1)
print(l)
l2 = np.append(l, [100,200,300])
print(l2)


print("once again", l)

l = np.append(l, [111,222])

print("last time", l)


pixel = np.array([[1,1],[2,2]])
pixel2 = np.array([[5,5],[6,6]])

print(pixel,'\n',pixel2)

pix = np.append(pixel, pixel2, axis=0)
pix2 = np.append(pixel,pixel2, axis=1)

print(pix,'\n',pix2)


#insert:-

a = np.array([1,2,3,4,5])
print(a)

b = np.insert(a, 2, [100,200])
print(b)


#Delete:-

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

b = np.delete(a,1, axis = 0)
c = np.delete(a,1, axis = 1)

print(b,'\n',c)


## FINDING IDX OF AN ARRAY WITH A VALUE:-

a = np.array([1,2,3,4,5,5,5,6,7,8,9])

print(np.where(a==1))

b = np.where(a==5)
print(b)
print(type(b))



#Indexing and Selection:-
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[1][2])
print(a[2,2])

print(a[1:,1:])


#Conditional Array:-

b = a>2
print(b)
print(a[b])
print(a>3)
print(a[a>3])

print(a)

a[a<=3] = 0
a[a>3] = 1

print(a)

#Numpy Operations:-
#Additions:-

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a+c)

#Similarly we can subtract, multiply, divide, scale:-

#Scaling:-

d = a+100

print(d)

# For more check numpy math operations online.






























