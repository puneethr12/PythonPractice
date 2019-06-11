# Numpy
import numpy as np

num= np.array([7, 8, 9])
#print(num)

#random

a=np.random.normal((2,2))
#print(a)

b=np.random.random((2,2))
#print(b)

#---------------------------
#loading text file as input
#---------------------------

x,y,z= np.loadtxt('C:\\Users\\training_b4b.01.20\\.PyCharmCE2019.1\\config\\scratches\\data.txt',skiprows=1,unpack=True)

#print((x))
#print((y))
#print((z))
#print(int(x[0]))

#------------------------------------------
array=np.array([[1,2,3,4],[5,6,7,8]])
#sum-----------
#print(array.sum())

#max-----------
#print(array.max())

#min-----------
#print(array.min())

#print(array.mean())

#print(np.median(array))

#standard deviation
#print(np.std(array))

#-----------append---------------------------------------

newarr=([2,3,4])

array1=np.append(newarr,[5,6])
#print(array1)

#--------insert
#print(np.insert(newarr,1,9))

#-----delete
#print(np.delete(newarr,[0]))

#-----arange
#print(np.arange(20,50,10))

#--------------------------------------------------------------
#Statistics
#---------------------------------

array1=np.arange(9).reshape([3,3])
#print(array1)
#print(np.max(array1))
#print(np.min(array1))
#print(np.median(array))

#standard deviation
#print(np.std(array))
#--------------------------------------------------------------------------------

#-------------------------------------------------------------------------
#----------- dot function/ used for matrix multiplication---------------
#---------------------------------------------------------------------
#print(np.dot(10,24))

a1=np.array([[1,2,3,4],[2,3,4,5]])
b1=np.array([[1,2,3,4],[2,3,4,5]])

b2=b1.reshape([4,2])

#print(np.dot(a1,b2))

f=np.array([1,3])
g=np.array([2,3])

#print(np.dot(f,g))

#----------------------------------------------------------------
#                      Numpy string Operations
#--------------------------------------------------------------------

#print(np.char.add(['Hello'],['world']))
#print('\n')
#print(np.char.add(['Hello'],[' world']))
#print('\n')
#print(np.char.add(['Hello'],[' numpy']),np.char.add([' in Python'],['ab']))

#print(np.char.multiply('python ',5))
#print(np.char.multiply('python \n',5))

#print(np.char.capitalize('hello python'))

#print(np.char.upper('hello python'))

#print(np.char.lower('HELLO'))

#print(np.char.replace('He is the legend','legend','King'))

#print(np.char.split('He is the Boss',' '))
#print(np.char.split('He is the Boss'))
#print(np.char.split('He is the Boss,King',','))


#print(np.char.splitlines('he is the king\n king of the world'))
#print(np.char.splitlines('he is the king\n king\r of the world'))      

#print(np.char.center('pytho1n',20, fillchar='*'))
#print(np.char.ljust('python',20, fillchar='*'))
#print(np.char.rjust('python',20, fillchar='*'))


#-SORT----------------------------------------------------
ary=np.array([1,24,5,78,423,2,56,8])
ary.sort()
#print(ary)

ary2=np.sort(ary)

ary3=sorted(ary)
#print(ary2)
#print(ary3)

#-------------------
a=np.array([[221,112,3],[19,120,23],[44,55,78],[99,102,303]])
#print(a)
#print(np.sort(a))

#-----------flatened sorting--------------------------------
#print(np.sort(a, axis=None))

#print(np.sort(a, axis=0))#columns are sorted

#print(np.sort(a, axis=1))#row content are sorted      

#--------------------------------------------------------------
#---------unicode int & str----------------------------------
#-------------------------------------------------------------

dt=np.dtype([('name', 'U10'), ('age',int)])
ab=np.array([('sanju', 19),('Rohit', 17),('Ishaan', 12)],dtype=dt)

#--- U10 is a unicode character used instead of string as ther is no str function
#print(ab)

#print(np.sort(ab, order='name'))


#---------------------------------------------------------
b=np.array([1,2,34,4,5,6,7])

#print(np.argmax(b))# index of max value

#print(np.argmin(b,axis=0))#index of min value

#------------------------------------------------
#  count
#--------------------------------------------------

#print(np.count_nonzero([[1,0,10],[2,0,4],[0,0,5]]))#total count
#print(np.count_nonzero([[1,0,10],[2,0,4],[0,0,5]],axis=0))# column wise count
#print(np.count_nonzero([[1,0,10],[2,0,4],[0,0,5]],axis=1))#row wise count

#-------------------------------------------------------------------
# Mtrix multiplication
#-------------------------------------------------------------------

m=np.array([[2,3],[3,2]])
n=np.array([[3,3],[1,2]])

print(np.matmul(m,n))

mn=([[1,2],[3,2]])
nm=([1,2])

print(mn)
print(nm)

print(np.matmul(nm,mn))

#----------------------------------------------------------------------------      






