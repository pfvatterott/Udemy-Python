import random

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]
print(states_of_america[random.randint(0, len(states_of_america) - 1)])

states_of_america[1] = "Pencilvania"

states_of_america.append("PaulLand")
print(states_of_america)

states_of_america.extend(["CarolLand", "HowdyLand"])
print(states_of_america)