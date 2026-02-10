#Write a program which provides the grades to the students based on their obtained marks out of 100 marks

marks=float(input("ENTER YOUR MARKS : "))
if(marks<40):
    print("YOUR GRADE : D (FAIL)",)
elif(marks<75 and marks>=40):
    print("YOUR GRADE : C")
elif(marks<90 and marks>=75):
 print("YOUR GRADE : B")
elif(marks>=90 and marks<=100):
 print("YOUR GRADE : A")
else:
 print("INVALID MARKS! ENTER CORRECT MARKS")
    