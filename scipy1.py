import scipy as sp

#----------------------Scipy----------------

def x(k):
    return k**2

#print(x(4))

f= lambda x:x**2
#print(f(5))
#--------------------------------------------
def adsb(m,n):
    if m>n:
        return m+n
    else:
        return m-n
#print(adsb(5,3))

#------------------------vector------------------
vec_adsb = sp.vectorize(adsb)
#print(vec_adsb([0,2,3],[4,5,2]))
#print(vec_adsb([10,32,43],[4,5,2]))


#--------array with ones-----------------------

a= sp.ones(3)
b= sp.ones([3,4])

zeros = sp.zeros([2,2])

#-----to get the matrix/array as integer use below expression
dtype=sp.ones([3,2],dtype=int)

#------------------------------
#print(dtype)
#print(zeros)
#print(a)
#print(b)

#----- empty array-----------
empti = sp.empty((2,3))

empa = sp.empty([2,3])

#print(empti)
#print(empa)
#print(type(empa))

#-------arange-------------
ra= sp.arange(10)

#print(ra)

rang = sp.arange(10,50)
#print(rang)

rang1 =sp.arange(1,20,2)
#print(rang1)

#--------1d array

ar=sp.arange(8)
#print(ar)

#----------2d array

ard= sp.arange(10).reshape(2,5)
#print(ard)

#---------3d array

ard3 = sp.arange(27).reshape(3,3,3)
#print(ard3)
#-------indexing in array------------------------------
x=sp.arange(10)**2

#print(x)
#print(x[3])
#print(x[2:6])

# iteration of x

#for i in x:
#    print(i)

#print(x.shape)
#print(type(x.shape))

#-------arithmetic array

m=sp.array([10,20,30,40])
n=sp.arange(4)

x= m +n
y= m-n
#print(x)
#print(y)

#------trignometric sin
#print(10*sp.sin(m))

#---- condition
#print(m<30)

#-----accessing the row/column in array

r=sp.arange(15).reshape([3,5])
#print(r)

#----to calculate sum of each column by specifying axis
#print(r.sum(axis=0))
#print(r.sum(axis=1))

#print(r.max(axis=1))
#print(r.max(axis=0))
#print(r.min(axis=1))
#print(r.min(axis=0))

#print(r.min())
#print(r.max())

#------------ matrix multiplication-/linear algebra
from scipy import linalg

sqmat=sp.array([[4,2],[9,5]])

# determinant
ans=linalg.det(sqmat)
#print(ans)


#---------scipy constants----

import scipy.constants
import math

print("scipy = value of pi = %.16f" %scipy.constants.pi)
print("math value of pi= %.16f" %math.pi)
print("speed of light in c=%.1F" % scipy.constants.c)

#--------random

sample = sp.random.normal(size=10)
#print(sample)

#--------mean, median,

#print("mean")
#print(sp.mean(sample))
#print("median")
#print(sp.median(sample))


#----------- size of an array

arr=[2,3,4,5,6,7,8]

print(sp.shape(arr))
print(sp.size(arr))

#-------- re-shape

ar1 = sp.array ([[2,3,4],[6,7,8]])

print(ar1)
print(ar1.reshape([3,2]))

#----------tuple-------------

mytup=(5,6,7,'Ind')

#print(mytup)

#packing
mytu=5,6,7,8,'Ind'
#print(mytu)
#print(type(mytu))

#unpacking
a,b,c,d,e=mytu

#print(a)
#print(b)
#print(c)
#print(d)






 







    

