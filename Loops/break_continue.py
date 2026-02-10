#Write two program where in one print the first number which is divisible by 7 and 5 both.....and in second program the squares of top 10 numbers except odd numbers....

#Program 1
i=1
while(i<=500):
    if(i%7==0 and i%5==0):
        print("The First Number divisible by both 5 and 7 is",i)
        break
        
    i+=1


#Program 2
k=1
while(k<=10):
       if(k%2==0):
            k+=1
            continue
       print(k**2)
       k+=1

             
