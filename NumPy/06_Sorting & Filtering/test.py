import numpy as np
vector=np.array([3,6,89,6,5,34,67,54,6,34])

# Sorting of Data
sorted_data=np.sort(vector)
print("1D Data :\n",sorted_data)

matrix=np.array([[1,2,6],[8,6,3],[9,4,3]])
matrix_sorted=np.sort(matrix,axis=0)
print("Row Wise Sort :\n",matrix_sorted)

matrix_sorted=np.sort(matrix,axis=1)
print("Column Wise Sort :\n",matrix_sorted)


# Filtering of Data
greater=vector>60
print(vector[greater])

# WHERE Clause in NumPy (Exactly same as ternary operator in C++)
data1=np.array([12,45,32,76,89,4,6,5,2,3,65,67,66,44,43,31,79])
filter_update=np.where(data1>50 , data1*(-1) , data1)
print("Where Clause Result :\n",filter_update)
 