import numpy as np

# .arange() method
data=np.arange(1,11)
print(f".arange method List :\n{data}")

# .linspace() method
data2=np.linspace(1,15,3)
print(f".linspace method List :\n{data2}")

# .reshape() method
array=np.arange(1,9)
print(f"Before Reshaping :\n{array}")
print(f"After Reshaping (4*2) :\n{array.reshape(4,2)}")
print(f"Again Reshaping (2*4) :\n{array.reshape(2,4)}")
print(f"Again Reshaping (8*1) :\n{array.reshape(8,1)}")
print(f"Again Reshaping (1*8) :\n{array.reshape(1,8)}")


# Generating random array series
random_array=np.random.random((3,3))
random_array=(random_array*9).astype(int)
print("Random Array :\n",random_array)
 