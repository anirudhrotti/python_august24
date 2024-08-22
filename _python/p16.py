<<<<<<< HEAD
#Program statement: Program to reverse the number

input_num = input("Enter the number to reverse it:")
reversed_num = ""
n = input_num
for i in range(len(input_num)):
    digit = int(n)%10
    #print(digit)
    reversed_num = reversed_num + str(digit) 
    n = int(n)/10
=======
#Program statement: Program to reverse the number

input_num = input("Enter the number to reverse it:")
reversed_num = ""
n = input_num
for i in range(len(input_num)):
    digit = int(n)%10
    #print(digit)
    reversed_num = reversed_num + str(digit) 
    n = int(n)/10
>>>>>>> c529d533494f9e76babeac19b475bf76a55c562a
print("The reverse of",input_num,"is",reversed_num)