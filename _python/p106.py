size=int(input('enter the size off elements'))

arr=[]
for i in range(size):
    arr.append(input('enter :'))

def insertsort(array):
    for i in range (1,len(array)):
        element=array[i]
        j=i-1
        while j>=0 and element < array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=element

    return array

x=insertsort(arr)
print(x)