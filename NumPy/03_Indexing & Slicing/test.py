import numpy as np

# 1D Array Slicing
array1=np.array([10,20,30,40,50,60,70,80,90,100])
print("Original Array :\n",array1)
print(f"Test-1 :\n{array1[:]}")
print(f"Test-2 :\n{array1[2:8]}")
print(f"Test-3 :\n{array1[1::3]}")
print(f"Test-4 :\n{array1[::2]}")
print(f"Test-5 :\n{array1[:8:2]}")
print(f"Test-6 :\n{array1[::-1]}")
print(f"Test-7 :\n{array1[4::-2]}")


# 2D Array Slicing
array2=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(f"\n\nOriginal Array :\n{array2}")
print(f"Test-1 :\n{array2[:]}")
print(f"Test-2 :\n{array2[0:2,0:3]}")
print(f"Test-3 :\n{array2[1:3,1:3]}")
print(f"Test-4 :\n{array2[::-1,::-1]}")
print(f"Test-5 :\n{array2[::-1,1:2]}")
