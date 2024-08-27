main_string=input('enter the string ')
compare_string=input("enter the string value to compare ")

test=list(main_string)
flag=0
for i in range(len(test)):
    c=test[0]
    del test[0]
    test.append(c)
    if list(compare_string)==test:
        flag=1
   
if flag ==1:
    print('1')
else:
    print('-1')     



 