import numpy as np
matrix=np.array([[12,45,67,78],[12,34,56,6]])
print(matrix)

# Properties of the Array
print(f"The dimension of the matrix is {matrix.ndim}")
print(f"The shape of the matrix is {matrix.shape}")
print(f"The size of the matrix is {matrix.size}")
print(f"The data type of the matrix is {matrix.dtype}")
print(f"Original Matrix :\n {matrix}\nAfter Transpose :\n{matrix.T}")


# Methods of the Array
zero_Matrix=np.zeros((3,4))
one_Matrix=np.ones((3,4))
scalar_Matrix=np.full((3,4),8)
print(f"Zero Matrix :\n{zero_Matrix}\nOne Matrix :\n {one_Matrix}\nScalar Matrix :\n{scalar_Matrix}")
