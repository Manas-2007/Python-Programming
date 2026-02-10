#Write a program to print the table of a given number

number=int(input("Enter the Number : "))
i=1
while(i<=10):
    print(number,"*",i,"=",number*i)
    i+=1
print("Loop Terminated")
