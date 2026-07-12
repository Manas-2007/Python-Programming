import numpy as np

# 1D Array Testing
d1=np.array([10,20,30,40,50])
d2=np.array([5,3,6,4,3])
print("Sum :",d1+d2)
print("Subtration :",d1-d2)
print("Multiplication :",d1*d2)
print("Divison :",d1/d2)
print("Floor Division :",d1//d2)
print("Exponent :",d1**d2)
print("Matrix Multiply :",d1@d2)

# 2D Array Testing
x=np.array([[4,3,6,7],[7,4,3,5],[6,1,2,3]])
y=np.array([[4,6,6,7],[9,3,4,5],[6,5,7,7]])
print(f"Sum :\n{x+y}")
print(f"Subtration :\n{x-y}")
print(f"Multiply :\n{x*y}")
print(f"Division :\n{x/y}")
print(f"Floor Division :\n{x//y}")
print(f"Exponent :\n{x**y}")

# 2D array (Scalar Operation)
items=np.array([[1,2,3,4],[5,6,7,8]])
items+=100;
print("Add :\n",items)
items=np.array([[1,2,3,4],[5,6,7,8]])
print("Exponenent :\n",items**2)
items=np.array([[1,2,3,4],[5,6,7,8]])
print("Multiply :\n",items*5)

