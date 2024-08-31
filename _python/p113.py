

def find_sum_of_digits(num):
    sum=0
    while num!=0:
        rem=num%10
        num=num//10
        sum=sum+rem
    return sum


input_num=int(input("enter a number :"))                                                                                                                                                                                                                                                                                                                                                                                                                                                        
sum_of_digits=find_sum_of_digits(input_num)
print(sum_of_digits)