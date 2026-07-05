import math

# Basic Function with Single Argument
def Square(n):
    return n**2;
print("The Square of 5 is",Square(5))

# Function with 2 arguments
def Multiple(a,b):
    return a*b;
print("The Multiplication of 2 & 5 is",Multiple(2,5));

# Function returning multiple values
def CircleStats(radius):
    area=math.pi*radius**2;
    circumference=2*math.pi*radius;
    return area,circumference;
a,b=CircleStats(5);
print(f"Area of Circle : {a:.2f} \nCircumference of Circle : {b:.2f}");

# Default value in argument
def Display(name="MANAS"):
    print("Hello,",name)
Display("PARI");
Display();

# Function with variable Positional Arguments (*args)
print("\n\nTesting *args :")
def Sum(*arg):
    sum=0;
    for i in arg:
        sum+=i;
    return sum;
print(Sum(1,2,3));
print(Sum(4,7,0,56,43));

# Function with key-value paired arguments (**kwargs)
print("\n\n**keyword Arguments concept : ");
def Display(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}");
Display(name="Manas");
Display(id=101,name="Manas Patidar",Branch="AIR");

# Concept of yield keyword (similar to return)
print("\n\nConcept of YIELD :")
def Print(x):
    for i in range(1,x+1,2):
        yield i;
result=Print(10);
print(result)
for i in result:
    print(i,end=" ");




