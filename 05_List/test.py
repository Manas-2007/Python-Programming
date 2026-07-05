list=["Manas","Gori","Pari","Ishanvi"];

#Linear Searching in List
isFound=False;
position=-1
for item in list:
    position+=1;
    if(item=="Ishanvi"):
        isFound=True;
        idx=position;
        break;
if(isFound):
    print("Item Available at Index",idx)
else:
    print("Item NOT found in List");


#Add from end of the list
list.append("Pooja");
print(list);

#Remove from end of the List
popped=list.pop();
print("Removed Item :",popped);
print(list)

#To remove a specific item
list.remove("Manas");
print(list)

#To add a specific item
list.insert(1,"MANAS");
print(list)

#To copy entire list WITH NEW REFERENCE IN MEMORY
list_copy=list.copy();      # Create a new copy
print(list);
print(list_copy);

#Generate a series of data in list (pattern based)
squared_nums=[x**2 for x in range(10)]
print(squared_nums)

