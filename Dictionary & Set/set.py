set1={10,20,30,40,50,10,20,40}
set2={10,70,60,80,90,100}
print("     Set 1 & Set 2")
print(set1)
print(set2)

print("\n       NUll set")
nullSet=set()
print(nullSet)

#Set methods
#1) Add and remove element
nullSet.add("Manas")
nullSet.add("Minakshi")
nullSet.add("Pooja")
print("\n       .add(): Add element in the set")
print(nullSet)

print("\n       .remove(): Remove element from set")
nullSet.remove("Manas")
print(nullSet)


#2)         .pop(): Removes random value from set
print("\n       .pop(): Removes random value from set")
random=nullSet.pop()
print(random)
print(nullSet)


#3)         .union(): Union of two sets
print("\n          .union(): Union of two sets ")
print(set1)
print(set2)
print("     Union of both above two sets")
print(set1.union(set2))



#4) .intersection: Common elements in two sets
print("\n      .intersection: Common elements in two sets ")
print(set1.intersection(set2))

