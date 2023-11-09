import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
randomName = names[random.randint(0, len(names) - 1)]
print(f"{randomName} is going to buy the meal today!")