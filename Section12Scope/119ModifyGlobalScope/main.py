enemies = 1

def increase_enemies():
    global enemies
    enemies = 2
    print(f'enemies inside function: {enemies}') # prints 2
    
increase_enemies()
print(f'enemies outside function: {enemies}') # prints 1


# Another way of adjusting global scope:
friends = 1
def increase_friends():
    return friends + 1

friends = increase_friends()
print(friends)
