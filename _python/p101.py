import math
no_load=int(input('enter no off elements'))


def read_elements(loadnumber):
    server1=[]
    server2=[]
    for i in range(loadnumber):
        load=int(input('enter server value'))

        if i%2 == 0 :
            server1.append(load)
        elif i %2 !=0:
            server2.append(load)

    return server1,server2
   


a,b=read_elements(no_load)

def check_load(list1,list2):
    sum1=sum(list1)
    sum2=sum(list2)

    if sum1 >0:
        print('server 1 is allocated')
    else:
        print('server 1 is diallocated')

    if sum2 >0:
        print('server 2 is allocated')
    else:
        print('server 2 is diallocated')

check_load(a,b)