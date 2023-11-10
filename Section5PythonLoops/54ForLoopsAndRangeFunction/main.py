for number in range(1, 10):
    print(number)
    # prints 1 - 9, so not the last digit
    
for number in range(1, 10, 3):
    print(number)
    # prints 1, 4, 7
    
total = 0
for number in range(1, 101):
    total += number
print(total)