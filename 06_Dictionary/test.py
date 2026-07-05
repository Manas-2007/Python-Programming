data={
    "id":101,
    "name":"Manas Patidar",
    "location":"Dubai",
    "CGPA":9.06
};
print(data);

#Add a new Key-value pair (direct by Key name with its value)
data["Stream"]="Finance";
print(data);

#Remove a key-value pair (ANY LOCATION using)
data.pop("id");
print("\n\nAfter Removing ID :\n",data);

#Remove a last key-value pair...(using .popitem())
data.popitem();
print("\n\nAfter Removing Last pair :\n",data)



#print only keys (NOT VALUES)
print("\n\nPrinting only keys:")
for i in data:
    print(i)

#print key-value pairs (using .items() method)
print("\n\nPrinting key-pair :")
for key,value in data.items():
    print(key,":",value)

#Auto generate pattern digits
print("\n\nGenerating Square Numbers : ");
square={x:x**2 for x in range(1,6)};
print(square);
