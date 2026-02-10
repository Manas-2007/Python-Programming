#Write a program which search for the target in the given list
list=["Manas","Vaishali","Shubham","Ashwin","Ashwini"]
target=input("Search Target : ")
k=False
for i in list:
    if(i==target):
        k=True
        break
    
if(k):
    print("ITEM AVAILABLE IN LIST")
else:
    print("ITEM NOT AVAILABLE IN LIST")
        
        
