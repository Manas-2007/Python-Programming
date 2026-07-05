name="Manas Patidar, Ishanvi Patidar";       #Immutable

print(name[0]);
print(name.lower());
print(name.upper());
print(len(name));               #Length of string


#Slicing of the string (Returns a portion of the string)
print(name[:])
print(name[0:])
print(name[:3])
print(name[2:4])


# (" ")formatted string print with Dynamic Data (format)
student={
    "name":"Manas Patidar",
    "city" :"Khargone",
};

display="I am {}, I am from {} district of \"MADHYA PRADESH\" ";
print(display.format(student["name"],student["city"]))



#String to List Conversion (split method)
list=name.split(",")
print(list)

#List to String Conversion (join method)
List=["Pooja","Hema","Ragini","Palak"];
print(" : ".join(List));
print(" ".join(List))
print("-".join(List))



# To identify the presence of the item in the list ('in' - keyword)
print("Pooja" in List)
print("MANAS" in List)




