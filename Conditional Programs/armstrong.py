#Write a program to check whether the number is armstrong or not (3-digit number)
number=int(input("ENTER 3-DIGIT NUMBER : "))
x=number%10
y=number//10%10
z=number//100
print("Digits:",x,y,z)
condition=(x*x*x)+(y*y*y)+(z*z*z)
if(condition==number):
    print("It's an ARMSTRONG Number")  
else:
    print("It's NOT an ARMSTRONG Number")


