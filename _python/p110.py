num=int(input('enter the digit '))

test_num=list(str(num))
print(test_num)
print(test_num.count('2'))
for i in range(len(test_num)):
    
    if test_num.count(test_num[i])>2:
        print('invalid digit')

