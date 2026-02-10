#Write a program to calculate the factorial of a given number
x=int(input("Enter Number : "))
fact=1
for i in range(1,x+1,1):
    fact=fact*i

print("The factorial of",x,"is",fact)