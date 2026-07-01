from test2 import Display, PrintEven;

# 1.File Importing and Function Calling
print('Hello Boys! Welcome to Python Programming.');
print('Importing function from file : test2.py');
Display('Pari');
PrintEven(10);


# 2.Dictionary (like objects in JavaScript)
data={
    "name": "Pari",     # JSON formatted
    "age": 20,
    "cgpa": 9.5
}
print("\n\nMy name is",data["name"],"and my age is",data["age"],"and my cgpa is",data["cgpa"],"\n\n");


# 3.List (like arrays in JavaScript)
data=[1,2,3,"Pari","Manas",56.45];
print(data);
for i in data:
    print(i);
print("\n\n");


# 4.While Loop
i=1;
while(i<10):
    print(i);
    i+=1;


# 5.Input Function
num1=int(input("\n\nEnter First Number : "));
num2=int(input("Enter Second Number : "));
print("The sum of",num1,"and",num2,"is",num1+num2);


# 6. If-Else Statement
age=int(input("\n\nEnter your age : "));
if(age<10 and age>0):
    print("You are a child");
elif(age>=18):
    print("You are an adult");

