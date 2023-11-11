def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"Nice weather here in {location}, right?")
    
greet_with("Paul", "Utah")
greet_with(location="Utah", name="Paul")
# These do the same thing. Typically, Python uses positional arguments but this is a way around it.