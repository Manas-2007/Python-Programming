#Write a program which calculates the average of even numbers upto 100

sum=0
for i in range(1,101,1):
    if(i%2==0):
        sum+=i

average=sum/50
print("The average of even numbers upto 100 is",average)

#Printing number of days
print("\n             DAYS IN A WEEK              ")
days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
for element in days:
    print(element)

print('\nLoop terminated')


