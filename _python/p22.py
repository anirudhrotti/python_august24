<<<<<<< HEAD
# Program statement: Program tp print X shape of N lines


num_lines = int(input("Enter the number of lines:"))
for i in range(num_lines):
    for j in range(num_lines):
        if j == i or j == num_lines-i-1:
            print("*",end=" ") 
        else:   
            print(" ",end=" ")
    
    print()

=======
# Program statement: Program tp print X shape of N lines


num_lines = int(input("Enter the number of lines:"))
for i in range(num_lines):
    for j in range(num_lines):
        if j == i or j == num_lines-i-1:
            print("*",end=" ") 
        else:   
            print(" ",end=" ")
    
    print()

>>>>>>> c529d533494f9e76babeac19b475bf76a55c562a
    