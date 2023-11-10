# Input a Python list of student heights
student_heights = "180 124 165 173 189 169 146".split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
totalHeight = 0
totalStudents = 0
for student_height in student_heights:
    totalHeight += student_height
    totalStudents += 1
average_height = round(totalHeight / totalStudents)
print(f"total height = {totalHeight}")
print(f"number of students = {totalStudents}")
print(f"average height = {average_height}")