print(int(8 / 3))
# prints 2, so not rounding up

print(round(8 / 3))
# prints 3

print(round(8 / 3, 2))
# prints 2.67

print(8 // 3)
# prints 2 without converting to int
# is also still an int

result = 4 / 2
result /= 2
print(result)
# prints 1.0

score = 0
score += 1


score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")