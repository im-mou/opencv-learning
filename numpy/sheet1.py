from numpy import *

def _p(param):
    print(param)

m = arange(15).reshape(3, 5)

_p(m)

_p(m.shape)
_p(m.size)
_p(m.ndim)
_p(m.dtype)
_p(m.itemsize)
_p(type(m))

# complex numbers
ca = array([[2,3],[4,5]], dtype=complex)
# _p(ca)



# shapes
z = zeros((3,4))
o = ones((4,2))
e = empty((1,2))

# _p(z)
# _p(o)
# _p(e)

# arange
r = arange(0, 1, 0.1)
# _p(r)


# reshape
rs = arange(10000).reshape(100, 100)
# _p(rs)


# operations
a = array([20, 30, 40, 50])
_p( a > 40 )


A = array([[1, 1], [0, 1]])
B = array([[2, 0], [3, 4]])

# element wise product
_p( A * B )

# matrix product
_p( dot(A,B) ) 


# upcasting
a = ones(3, dtype=int32)
b = linspace(0, pi, 3)
c = a+b
d = exp(c*1j)

_p(b)
_p(c)
_p(d)


# random
r = random.random((3,3))

# _p(r)
# _p(r.sum())
# _p(r.min())
# _p(r.max())


# axis operations
# _p(r.sum(axis=0)) # sum of each column
# _p(r.min(axis=1)) # min of each row
# _p(r.cumsum(axis=1)) # cumulative sum along each row


# slicing
a = arange(10)**3

# _p(a[:])
# _p(a[2:5])


# a[:6:2] = -1000 # a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
# _p(a)

# _p(a[::-1])

# dimensions# new axis 
a = array([0, 1, 2])
b = ones((3, 5))
c = arange(3, 9)

# _p(a[..., newaxis] * c)
# _p(a.shape)
# _p(a[..., newaxis].shape)
# _p(a[newaxis, ...].shape)


# indices
# _p(indices((2, 3)))

# shape manipulation
a = floor(10 * random.random((3,4)))
# _p(a)

# # flatten the array
# _p(a.ravel())

# # transpose
# _p(a.T)

# resize
a = array([[ 7.,  5.],[ 9.,  3.],[ 7.,  2.],[ 7.,  8.],[ 6.,  8.],[ 3.,  2.]])
# _p(a.reshape((2,-1)))



# stacking
a = floor(10*random.random((2,2)))
b = floor(10*random.random((2,2)))

# vertical stack
_p(vstack((a, b)))

#horizontal stack
_p(hstack((a, b)))

# column stack
_p(column_stack((a, b)))


a = array([4., 3.])
b = array([2., 8.])

_p(row_stack((a,b)))
_p(column_stack((a[:, newaxis], b[:, newaxis])))
_p(vstack((a[..., newaxis], b[..., newaxis])))

# Copies and views

a = arange(12).reshape(3, 4)

c = a.view()

_p(c.base is a)
_p(c)

# changing c's shape, a's shape won't change
c.shape = 2, 6
c[0,4] = 10000 # this WILL change the value of 'a'

_p(a)

# Deep copy, create a new independent object
d = a.copy()
_p(d.base is a)
