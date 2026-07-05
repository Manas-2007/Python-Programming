class Bank:
    def __init__(self):
        self.username="";
        self.pin="";
        self.balance=0;

    def Registration(self):
        print("Register yoor Account here :");

        while(True):
            username=input("Enter Username :").strip();
            pin=input("Set Pincode :").strip();
            confirm_pin=input("Re-Enter Pincode :");

            if(username=="" or pin=="" or confirm_pin==""):
                print("All Fields Mandatory....Try again");
            elif(pin!=confirm_pin):
                print("Pincode does NOT match...Try again");
            else:
                self.username=username;
                self.pin=pin;
                print("Registation successfull");
                break;

    def Login(self):
        print("Login your account : ");
        while(True):
            username=input("Enter Username : ").strip();
            pin=input("Enter Pincode :").strip();
            if(username=="" or pin==""):
                print("All fields Mandatory...Try again");
            elif(username==self.username and pin==self.pin):
                print("Login Successfull");
                break;
            else:
                print("Invalid Credentials...Try again");
                
    def Pin_Check(self):
        while(True):
            pin=input("Enter Pincode :").strip();
            if(pin==""):
                print("Pincode is Mandatory...");
            elif(pin==self.pin):
                print("=======ACCESS GRANTED========");
                break;
            else:
                print("Incorrect Pin...Try again");
                
                
    def Information(self):
        self.Pin_Check();
        print("Username :",self.username);
        print("Current Balance :",self.balance);
            
    def Deposit(self):
        self.Pin_Check();
        while(True):
            amount=int(input("Enter Deposit Amount :"));
            if(amount<=0):
                print("Invalid Amount...Try again");
            elif(amount>0):
                self.balance+=amount;
                print("Deposit Successfull");
                break;
            
    def Withdraw(self):
        self.Pin_Check();
        while(True):
            amount=int(input("Enter Withdraw Amount :"));
            if(amount<=0):
                print("Invalid Amount...Try again");
            elif(amount>self.balance):
                print("Insuffient Balance...");
            elif(amount<=self.balance):
                self.balance-=amount;
                print("Withdraw successfull");
                break;
            
    def Balance_Check(self):
        self.Pin_Check();
        print(f"Current Balance : {self.balance}");
            

# Actual implementation     
user=Bank(); 
user.Registration();
user.Login();      
print("====================WELCOME TO FINANCE BANKING SYSTEM================================");
choice=0;
while(choice!=5):
    print("1.Account Holder Information\n2.Deposit Amount\n3.Withdraw Amount\n4.Balance Check\n5.Exit");
    choice=int(input("Select choice :"));
    if(choice==1):
        user.Information();
    elif(choice==2):
        user.Deposit();
    elif(choice==3):
        user.Withdraw();
    elif(choice==4):
        user.Balance_Check();
    
    print("Exiting..........");
    




    

    