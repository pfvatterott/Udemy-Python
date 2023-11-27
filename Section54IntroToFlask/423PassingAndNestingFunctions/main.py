def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)
    
    
# Functions as first-class objects 
    
result = calculate(add, 2, 3)
# print(result)


# Nested functions

# def outer_function():
#     print("I am outer")
    
#     def nested_function():
#         print("I am inner")
        
#     nested_function()
        
        
# outer_function()

# Functions can be returned from other functions

def outer_function():
    print("I am outer")
    
    def nested_function():
        print("I am inner")
        
    return nested_function
        
        
inner_function = outer_function()
inner_function()