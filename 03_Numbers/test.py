import random;
import math;
data=["Manas","Ishanvi","Gori"];
i=1;
while(i<=10):
    print(random.choice(data));
    i+=1;


#Ceil provides Greater integer value
print(math.ceil(3.6));
print(math.ceil(3));

#Floor provides Smaller integer value
print(math.floor(3.6));
print(math.floor(3.1));

#Trunc provides the value nearest to 0
print(math.trunc(3.2));
print(math.trunc(-5));
print(math.trunc(-6.7));

