import random
import myModule

randomNumber = random.randint(1, 5)
print(randomNumber)
print(myModule.pi)

random_float = random.random() # random between 0.0 and 1.0
print(random_float)

random_float_2 = random.randint(1, 5) * random.random()
print(random_float_2)