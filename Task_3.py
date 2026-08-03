import numpy as np

a = np.array([[1, 5, 2], [4, 4, 5], [8, 9, 6]])
b = np.array([[8, 6, 7], [6, 5, 2], [6, 8, 7]]) # Arrays in Numpy

print("A: ", end="")
print(a[0], "      ", "B:", b[0])
for i in range(1, len(a)):
    print("   ", a[i], "         ", b[i])# printing the Arrays

# Indexing syntax: arr[start:stop:step]
print(f"Sub-array of a: {a[0:2, 1:3]}") # Accessing a sub-array from row 0 to 1 and column 1 to 2
print(f"Sub-array of b: {b[1:, 0:2]}") # Accessing a sub-array from row 1 to end and column 0 to 1

print("Performing mathematical operations on arrays")
print(f"a + b: {a + b}")
print(f"a - b: {a - b}")

print(f"Array a statistics:") #Complex calculations using Numpy functions
print(f"Sum: {a.sum()}, Mean: {a.mean()}, Min: {a.min()}, Max: {a.max()}")
print(f"Array b statistics:")
print(f"Sum: {b.sum()}, Mean: {b.mean()}, Min: {b.min()}, Max: {b.max()}")

print("NUMPY FUNDAMENTALS COMPLETED!")