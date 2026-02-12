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



#Discussing various dictionary methods:

#1) Accessing keys 
print("\n       .keys(): to access only keys")
print(list(student.keys()))


#2) Accessing only values of the keys:
print("\n       .values(): Only values of keys")
print(list(student.values()))

#3) Accessing all keys and values
print("\n      .items(): to access all pairs")
print(list(student.items()))

#4) Access particular values of the key
print("\n    To access value of key")
print(student["Name : "])
print(student["Subjects :"])

#5) To update the dictionary or add new key
print("\n       Update dictionary/insert new key")
student.update({"Name ":"Muskan"})
print(student)


