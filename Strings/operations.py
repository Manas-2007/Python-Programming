#calculating the length of the string also print it character by character

string=input("ENTER SENTENCE : ")



#Length of string (using len(string_name) function)
print("\nLength of String : ",len(string))



#Print ch by ch
print("         Printing Ch by Ch               ")
for i in range(0,len(string),1):
    print(string[i])



#Slicing of the string [Starting idx : Ending Idx]......but ending idx not included
print("         String Slicing Function             ")
slicestr=string[1:3]                
print(slicestr)



#Concept of Negative Indexex
print("             Concept of Negative Indexing                ")
name="Manas"        #name[-5:-1]
print(name[-5:])        #Manas
print(name[-5:-1])      #Mana
print(name[-5:-2])      #Man
print(name[-5:-3])      #Ma



#String end with function to check string ending characters
print("\n               String ENDWITH function             \n")
sentence="I am Manas Kumar Patidar"
print(sentence.endswith("kum"))         #False
print(sentence.endswith("dar"))         #True



#String replace function
print("\n           String REPLACE function             \n")
string="I am studying Python from apna college"
print(string.replace("o","a"))
print(string.replace("Python","Javascript"))


#Find the index of particular word or character
print("\n                   Find function Working\n")
name="I am Manas Patidar"
print(name.find("am"))
print(name.find("Manas"))
print(name.find("M"))
print(name.find("priya"))           #If not available written -1


#Count function : used for counting the substring from the string (Occurance)
print("\n               Working of the COUNT function\n")
name="I am Manas Patidar, I am studying Python from Apna College."
print(name.count("am"))
print(name.count("Apna"))
print(name.count("a"))





