<<<<<<< HEAD
#Problem statement: Program to Find the biggest (smallest) digit in a number

input_num = input("Enter the number to Find the largest digit:")
#print(max(input_num))

n = len(input_num)
largest = input_num[0]
for i in range(1,n):
    if input_num[i]>largest:
        largest = input_num[i]
=======
#Problem statement: Program to Find the biggest (smallest) digit in a number

input_num = input("Enter the number to Find the largest digit:")
#print(max(input_num))

n = len(input_num)
largest = input_num[0]
for i in range(1,n):
    if input_num[i]>largest:
        largest = input_num[i]
>>>>>>> c529d533494f9e76babeac19b475bf76a55c562a
print("The largest digit in",input_num,"is",largest)