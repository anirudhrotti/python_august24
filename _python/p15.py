<<<<<<< HEAD
#Program statement: Program to Find sum even(odd) digits in a number

sum_num = input("Enter number to find the sum of its even digits:")
sum_digits = 0
for i in sum_num:
    if int(i)%2 == 0:
        sum_digits += int(i)
=======
#Program statement: Program to Find sum even(odd) digits in a number

sum_num = input("Enter number to find the sum of its even digits:")
sum_digits = 0
for i in sum_num:
    if int(i)%2 == 0:
        sum_digits += int(i)
>>>>>>> c529d533494f9e76babeac19b475bf76a55c562a
print("The sum of even digits in",sum_num,"is",sum_digits)