# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]

# name = "Angela"
# new_list = [l.lower() for l in name]


# new_list = [n * 2 for n in range(1,5)]


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [name for name in names if len(name) < 5]

new_list = [name.upper() for name in names if len(name) > 4]


print(new_list)