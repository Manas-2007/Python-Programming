data={1,2,3,4,3,2,1,"Manas","Manas","Ishanvi"};

#Duplicate entries NOT allowed (even length method ignores it)
print(data);
print(f"Length of the set :{len(data)}");

# Empty set
items={"M","A"};
empty_dict={};
empty_set=set();            #Empty set (NOT {} )
print(f"Empty Set 'set()' :{type(empty_set)}");
print(f"Empty Dictionary : {type(empty_dict)}");

#Set Methods
empty_set.add("Manas");
empty_set.add("Gori");
empty_set.add("Ishanvi");
print("\n\n",empty_set)
print("After REMOVING :");
empty_set.remove("Manas");
print(empty_set);

#Empty the set : .clear();
# Remove a RANDOM VALUE from the set : .pop()

# Union & Intersection
print("\n\nUNION OF SETS");
s1={1,2,3,4,5,3,2};
s2={"Manas","Gori",4,5,3,2};
UNION=s1.union(s2);
INTERSECTION=s1.intersection(s2);
print(UNION);
print("\nINTERSECTION OF SETS");
print(INTERSECTION)

