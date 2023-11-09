print("The Love Calculator is calculating your score...")
name1 = "Angela Yu" # What is your name?
name2 = "Jack Bauer" # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


combinedName = name1.lower() + name2.lower()
trueScore = combinedName.count("t")
trueScore += combinedName.count("r")
trueScore += combinedName.count("u")
trueScore += combinedName.count("e")

loveScore = combinedName.count("l")
loveScore += combinedName.count("o")
loveScore += combinedName.count("v")
loveScore += combinedName.count("e")

totalScore = (trueScore * 10) + loveScore
if totalScore < 10 or totalScore > 90:
    print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore > 40 and totalScore < 50:
    print(f"Your score is {totalScore}, you are alright together.")
else:
    print(f"Your score is {totalScore}.")

