para_input=list(input("enter the example "))

print(para_input)

open_count=[]
close_count=[]
for i in range (len(para_input)):
    if para_input[i] == "(":
        open_count.append(para_input[i])
    elif para_input[i] == ")":
        close_count.append(para_input[i])
    if len(open_count)<len(close_count):
        print('improper arrangment')
        break

if len(open_count)==len(close_count)!=0:
    print("proper arrangements")
else:
    print("improper arrangements")




