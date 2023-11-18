

file_1_list = []
with open("Section26ListComprehension\\238DataOverlap\\file1.txt") as file_1:
    file_1_list = file_1.readlines()
file_1_list = [int(num.replace("\n", "")) for num in file_1_list]

file_2_list = []
with open("Section26ListComprehension\\238DataOverlap\\file2.txt") as file_2:
    file_2_list = file_2.readlines()
file_2_list = [int(num.replace("\n", "")) for num in file_2_list]


result = [n for n in file_1_list if n in file_2_list]
print(result)


# Write your code above 👆
# print(result)
