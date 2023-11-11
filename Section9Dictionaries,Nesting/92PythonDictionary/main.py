programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    123: "testing"
}

print(programming_dictionary["Bug"])
print(programming_dictionary[123])

programming_dictionary["new_value"] = "testingtesting"
programming_dictionary["Bug"] = "new value for bug"
print(programming_dictionary)

empty_dictionary = {}
empty_dictionary["first_key"] = "first_value"


for thing in programming_dictionary:
    print(thing)
    # prints just the keys, no values

for thing in programming_dictionary:
    print(programming_dictionary[thing])
    # prints the values