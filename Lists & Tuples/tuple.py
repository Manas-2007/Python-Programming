#Tuple is same as List but is it immutable like string....but list is mutable in nature

tup=(10,20,30,40,50)
print("         TUPLE DATA LIST")
print(tup)

print("\n       ACCESSING THE ELEMENT FROM TUPLE")
for i in range(0,len(tup),1):
    print(tup[i])

#Tuple methods

#1) Index method: to identify the index of the particular element in the tuple
names=("Manas","Kusum","Suman","Manas","Manas","Kamal")
print("\n            DATALIST OF TUPLE")
indexno=names.index("Suman")
print(indexno)


#2) count method: to calculate the occurance of a particular element in the tuple
print("\n       FREQUNCY COUNT METHOD")
countno=names.count("Manas")
print(countno)



