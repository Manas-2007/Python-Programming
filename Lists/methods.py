#Various methods of lists


#1) SORTING METHODS
marks=[40,76,34,99,2,56,89,33]
print("     Original List           ")
print(marks)
print("\n     Ascending Ordered List")
marks.sort()
print(marks)
print("\n     Descending Ordered List")
marks.sort(reverse=True)
print(marks)


#2)ACCCESING ELEMENTS
names=['Manas','Meghna','Pushkar','Bhavesh','Sunita']
print("\n\n      ACCESSING ELEMENTS FROM THE LIST")
for i in range(0,len(names),1):
        print(names[i])


#3)Reverse entire list
print("\n           REVERSING LIST  ")
print("Original List")
even_intergers=[24,68,44,28]
print(even_intergers)
even_intergers.reverse()
print("After Reversing")
print(even_intergers)


#4Insertion and deletion in list
numbers=[11,12,13,14,15]
print("\n       INSERTION & DELETION IN LIST")
print("Original List")
print(numbers)
value=500
numbers.insert(1,value)
print("List after Insertion")
print(numbers)
numbers.remove(500)
print("After Deletion List")
print(numbers)
