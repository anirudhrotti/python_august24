<<<<<<< HEAD
#Program statement: Program to find odd place even digits

input_num = input("Enter the number to find odd place even digits:")
odd_placed = []
for i in range(len(input_num)):
    if i%2 == 0:
        if int(input_num[i])%2 == 0:
            odd_placed.append(input_num[i])
=======
#Program statement: Program to find odd place even digits

input_num = input("Enter the number to find odd place even digits:")
odd_placed = []
for i in range(len(input_num)):
    if i%2 == 0:
        if int(input_num[i])%2 == 0:
            odd_placed.append(input_num[i])
>>>>>>> c529d533494f9e76babeac19b475bf76a55c562a
print("The odd placed even digits are:",odd_placed)