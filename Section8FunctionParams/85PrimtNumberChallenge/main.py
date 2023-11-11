# Write your code below this line 👇

def prime_checker(number):
    isPrime = True
    for index in range(2, number):
        if number % index == 0:
            isPrime = False
    if isPrime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        



# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int("4") # Check this number
prime_checker(number=n)