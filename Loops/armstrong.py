#Write a program to print a armstrong number upto 1000
count=1
while(count<1000):
    x=count%10
    y=count//10%10
    z=count//100
    if((x*x*x)+(y*y*y)+(z*z*z)==count):
        print(count)
    count+=1
print("Loop Ended\n")    