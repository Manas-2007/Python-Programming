amazon={
    "id":1,
    "Product":"T-Shirt",
    "Price":560,
    "is_bought":False
}
print("\n      Normal Dictionary")
print(amazon)
print(list(amazon))
print(tuple(amazon))

print("\n       Nested Dictionary")
student={
    "Roll_No. : ":101,
    "Name : ":"Manas Kumar",
    "Subjects :":{
        "C++ : ":95,
        "Maths :":89,
        "AI : ":98
    }
}
print(student)
print(list(student))
print(tuple(student))
print("         Accessing only subjects with marks")
print(student["Subjects :"])

#Discussing various dictionay methods:
