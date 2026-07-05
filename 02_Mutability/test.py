#Case-1 (Independent)
l1=[1,2,3,4];
l2=[1,2,3,4];
print("L1 :",l1,"\nL2 :",l2);

l1[0]="Mishti";
print("\nAfter Update")
print("L1 :",l1,"\nL2 :",l2);



# Case-2 (Linked with each other)
l1=[1,2,3,4];
l2=l1;
print("\n\nL1 :",l1,"\nL2 :",l2);

l2[2]="Pari";
print("\nAfter Update")
print("L1 :",l1,"\nL2 :",l2);

# Case-3 (Slicing - Copy Created/Independent Behaviour)
l1=[1,2,3,4];
l2=l1[:];
print("\n\nL1 :",l1,"\nL2 :",l2);

l2[2]="Pari";
print("\nAfter Update")
print("L1 :",l1,"\nL2 :",l2);


# reference concept 
print('\n\nReference Concepts')
m=[1,2,3,4,5];
n=[1,2,3,4,5];
print(m==n);            #( == )compared only VALUES
print(m is n);          #( is )compares Reference in Memory

a=[1,2,3,4,5];
b=a;
print(a==b);
print(a is b);






