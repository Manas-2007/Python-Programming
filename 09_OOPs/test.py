class Car:

    # Parameterized constructor
    def __init__(self,brand,model):
        self.brand=brand;
        self.model=model;
    
    # Member function 
    def Display(self):
        print("Brand :",self.brand);
        print("Model :",self.model);

#Inheritance
class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model);
        self.battery_size=battery_size;

    def Display(self):
        super().Display();
        print("Battery Size :",self.battery_size);




# Creating object
my_Electric=Electric_Car("Ola","Scooty","400 volt");
my_Electric.Display();
print("Brand of the Car is",my_Electric.brand)