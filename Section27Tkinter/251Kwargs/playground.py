# def calculate(**kwargs):
    
#     print(kwargs) 
#     # {'add': 3, 'multiply': 5}
    
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
    
    
#     print(kwargs["add"])
    
    
# calculate(add=3, multiply=5)





def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(kwargs)
    print(n)
    
    
    
calculate(2, add=3, multiply=5)



class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # if make isn't passed as an arg, no error
        self.model = kw.get("model")
        
        
my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)