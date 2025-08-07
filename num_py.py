print("NUMPY")
print("")

"""
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.

In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.
"""

import numpy as np

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Nested array
arr = np.array(42) # 0-D
print(arr)

arr = np.array([1, 2, 3, 4, 5]) # 1-D
print(arr)

arr = np.array([[1, 2, 3], [4, 5, 6]]) # 2-D
print(arr)

print(arr.ndim) # We can check the number of dimensions with ndim

arr = np.array([1, 2, 3, 4], ndmin=5) # We can use ndim to set dimensions

print(arr)
print('number of dimensions :', arr.ndim)

# Array Idexes
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3]) # Positions 3 and 4 in a 1-D Array

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

arr = np.array(
  [
    [ # Group 0
      [1, 2, 3], # Row 0
      [4, 5, 6] # Row 1
    ],
    [ # Group 1
      [7, 8, 9], # Row 0
      [10, 11, 12] # Row 1
    ]
  ]
)
print(arr[0, 1, 2]) # Position 2 in Row 1 in Group 0 -> 6
"""
0 -> First Dimension
1 -> Second array in the dimension
2 -> Third position in the array
"""

# Slicing array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) # From position 1 (included) to 5 (excluded)
print(arr[4:]) # From position 4 (included) to the end
print(arr[:4]) # From start to position 4 (excluded)

# You can also use negative indexes

# Step
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) # Return from index 1 to 5 using 2 steps
"""
pos 1 -> 2
pos 5 -> 6 (excluded)
steps -> [2, 4]
"""
print(arr[::2]) # From index 0 to 7 using 2 steps

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) # From the second element, slice elements from index 1 to index 4 (not included)
print(arr[0:2, 2]) # From both elements, return index 2
print(arr[0:2, 1:4]) # From both elements, slice index 1 to index 4 (not included), this will return a 2-D array

# Copy vs View array
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr) # [42  2  3  4  5]
print(x) # [1 2 3 4 5]

y = arr.view()
y[0] = 31

print(arr) # [31  2  3  4  5]
print(y) # [31  2  3  4  5]

# Array shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape) # 2 Dimensios, 4 items

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape) # shape of array : (1, 1, 1, 1, 4)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3) # Reshape in 2 dimesions, 4 rows, 3 items
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2) # Reshape to 2 arrays that contain 3 arrays with 2 items
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3) Error -> cannot reshape array of size 8 into shape (3,3)
# print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

newarr = arr.reshape(2, 2, -1)
print(newarr)
"""
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
"""

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr) # [1 2 3 4 5 6]

# Loop an array
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
"""
[1 2 3]
[4 5 6]
"""

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

# Concatenate arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))

print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
"""
[[1 2 5 6]
 [3 4 7 8]]
"""

arr = np.stack((arr1, arr2), axis=1)
print(arr)
"""
[[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
"""

# Split array
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3) # [array([1, 2]), array([3, 4]), array([5, 6])]
print(newarr)

newarr = np.array_split(arr, 4) # [array([1, 2]), array([3, 4]), array([5]), array([6])]
print(newarr)

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
"""
[array([[1, 2],
       [3, 4]]), array([[5, 6],
       [7, 8]]), array([[ 9, 10],
       [11, 12]])]
"""

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
"""
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
"""

# Search in arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4) # Find the indexes where the value is 4
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0) # Find the indexes where the values are even
print(x)

# Sort array
arr = np.array([3, 2, 0, 1]) # [0 1 2 3]
print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))
"""
[[2 3 4]
 [0 1 5]]
"""

# Filter
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]

print(newarr)

arr = np.array([41, 42, 43, 44])

filter_arr = []

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)