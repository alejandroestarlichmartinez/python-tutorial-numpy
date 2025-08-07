
print("UFUNC")
print("")

"""
ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

ufuncs also take additional arguments, like:
  - where boolean array or condition defining where the operations should take place.
  - dtype defining the return type of elements.
  - out output array where the return value should be copied.

Vectorization -> Converting iterative statements into a vector based operation is called vectorization.
"""

import numpy as np

# Without ufunc
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print(z)

# Creating an ufunc
"""
frompyfunc() method takes the following arguments:
  - function - the name of the function.
  - inputs - the number of input arguments (arrays).
  - outputs - the number of output arrays.
"""
def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# Simple arithmetic
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2) # Add functions
print(newarr)

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2) # Subtracts the values from one array with the values from another array, and return the results in a new array.
print(newarr)

# Rounding decimals
arr = np.trunc([-3.1666, 3.6667]) # Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
print(arr) # 

arr = np.around(3.1666, 2) # The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
print(arr)

arr = np.floor([-3.1666, 3.6667]) # The floor() function rounds off decimal to nearest lower integer.
print(arr)

arr = np.ceil([-3.1666, 3.6667]) # The ceil() function rounds off decimal to nearest upper integer.
print(arr)

# Logs - NumPy provides functions to perform log at the base 2, e and 10.
arr = np.arange(1, 10)
print(np.log2(arr))

arr = np.arange(1, 10)
print(np.log10(arr))

# Summations - Addition is done between two arguments whereas summation happens over n elements.
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2) # [2 4 6]
print(newarr)

newarr = np.sum([arr1, arr2]) # 12
print(newarr)

newarr = np.sum([arr1, arr2], axis=1) # If you specify axis=1, NumPy will sum the numbers in each array. [6 6]
print(newarr)

arr = np.array([1, 2, 3])
newarr = np.cumsum(arr) # [1, 1+2, 1+2+3]
print(newarr)

# Products
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod(arr1) # 1*2*3*4 = 24
print(newarr)

newarr = np.prod([arr1, arr2]) # 1*2*3*4*5*6*7*8 = 40320
print(newarr)

newarr = np.prod([arr1, arr2], axis=1) # [24, 1680]
print(newarr)

newarr = np.cumprod(arr1) # [1, 1*2, 1*2*3, 1*2*3*4] [1 2 6 24]
print(newarr)

# Diferences
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr) # [5 10 -20] because 15-10=5, 25-15=10, and 5-25=-20
print(newarr)

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2) # n means repeatance -> 15-10=5, 25-15=10, and 5-25=-20 then 10-5, -20-10 = [5, 30]
print(newarr)

# Finding LCM (Lowest Common Multiple)
num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print(x)

# In arrays 
arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)
print(x) # 18

# Finding GCD (Greatest Common Devisor)
num1 = 6
num2 = 9

x = np.gcd(num1, num2)
print(x)

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)
print(x)

# Trigonometric
x = np.sin(np.pi/2)
print(x) # 1.0

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x) # [1.         0.8660254  0.70710678 0.58778525]

# Degrees to Radians
arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)
print(x) # [1.57079633 3.14159265 4.71238898 6.28318531]

# Radians to degrees
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)
print(x) # [ 90. 180. 270. 360.]

# Finding angles
x = np.arcsin(1.0) # NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
print(x) # 1.5707963267948966

# Angles of Each Value in Arrays
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x) # [ 1.57079633 -1.57079633  0.10016742]

# Hypotenues - NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.
base = 3
perp = 4
x = np.hypot(base, perp)
print(x) # 5.0

# Hyperbolic
x = np.sinh(np.pi/2) # NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
print(x) # 2.3012989023072947

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr) # [2.50917848 1.60028686 1.32460909 1.20397209]
print(x)

# Finding Angles
x = np.arcsinh(1.0)
print(x) # 0.881373587019543

arr = np.array([0.1, 0.2, 0.5])
x = np.arctanh(arr)
print(x) # [0.10033535 0.20273255 0.54930614]

# Sets
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr) # [1 2 3 4 5 6 7]
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print(newarr) # [1 2 3 4 5 6]

newarr = np.intersect1d(arr1, arr2, assume_unique=True) # Method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
print(newarr) # [3 4]

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr) # [1 2]


newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr) # [1 2 5 6]