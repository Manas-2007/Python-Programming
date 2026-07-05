# decorator function
def Display_Hello(func):
    def wrapper(*args):
        print("Hello World");
        func(*args);
    return wrapper;

@Display_Hello
def addition(a,b):
    print(f"The Sum of {a} & {b} is {a+b}");


@Display_Hello
def subtration(a,b):
    print(f"The Sub of {a} & {b} is {a-b}");


# Working of Decorator
addition(4,5);

subtration(6,3);