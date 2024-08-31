import pdb
pdb.set_trace()
input_num=int(input('enter number for its factorial :'))
cho=int(input('enter choice 1=recurcive,2=iterative :'))

def find_factorial_recursively(num):
    if num==0 or num==1:
        return 1
    
    return num*find_factorial_recursively(num-1)

def find_fact_iteratively(num):
    factoria_num=1
    if num==0 or num==1:
        return factoria_num
    for i in range(2,num+1):
        factoria_num=factoria_num*i

    return factoria_num


if cho==1:
    fact=find_factorial_recursively(input_num)
elif cho==2:
    fact=find_fact_iteratively(input_num)

print(fact)
