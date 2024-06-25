#1 Install Numpy: open new terminal in Vs code
#               : make sure pip is intalled
#               : Type pip install numpy  

#2.Importing NumPy:
import numpy as np


#3.Creating NumPy arrays:
"""NumPy's main object is the homogeneous multidimensional array. Let's create some:"""
# Create a 1D array
arr1 = np.array([1, 2, 3, 4, 5])

# Create a 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])


#4.Array attributes:
"""NumPy arrays have several useful attributes:"""
print(arr1.shape)  # Output: (5,)
print(arr2.shape)  # Output: (2, 3)
print(arr1.dtype)  # Output: int64


#5. Array creation functions:
"""NumPy provides functions to create arrays with placeholder content:"""
zeros = np.zeros((3, 3))  # 3x3 array of zeros
ones = np.ones((2, 4))    # 2x4 array of ones
random_arr = np.random.rand(2, 2)  # 2x2 array of random values

print(zeros)
print(ones)
print(random_arr)

#6. Array indexing and slicing:
"""You can access and modify array elements:"""
print(arr1[0])  # First element
print(arr2[0, 1])  # First row, second column
print(arr1[1:4])  # Slice from index 1 to 3


#7.Array operations:
"""NumPy allows element-wise operations on arrays:"""
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Element-wise addition
print(a * b)  # Element-wise multiplication
print(a ** 2)  # Element-wise squaring

#8.Broadcasting:
"""NumPy can operate on arrays of different shapes:"""


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([10, 20, 30])

print(a + b)  # b is broadcast to match a's shape


#9.Array manipulation:
"""Reshape, concatenate, and split arrays:"""
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))
print(concatenated)

split = np.split(concatenated, 2)
print(split)


#10. Mathematical functions:
"""NumPy provides various mathematical functions:"""
a = np.array([0, 30, 45, 60, 90])
print(np.sin(a * np.pi / 180))  # Sine of angles in degrees
print(np.mean(a))  # Mean of array
print(np.max(a))   # Maximum value

#11. Linear algebra operations:
"""NumPy has a submodule for linear algebra:"""
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.dot(a, b))  # Matrix multiplication
print(np.linalg.det(a))  # Determinant
print(np.linalg.inv(a))  # Inverse


#12.Reading and writing files:
"""NumPy can read and write arrays to files:"""

arr = np.array([1, 2, 3, 4, 5])
np.save('my_array.npy', arr)  # Save to .npy file
loaded_arr = np.load('my_array.npy')  # Load from .npy file
