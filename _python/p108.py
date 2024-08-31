def partition_sort(arr):
    pivot=arr[1]
    j=0
    for i in range (len(arr)-1):
        if arr[i]<pivot:
            arr[j],arr[i]=arr[i],arr[j]
            j=j+1

    arr[j],arr[-1]=arr[-1],arr[j]
                                
    return arr



x=[1,12,3,4,23,4,1,43]
print(x)
ans=partition_sort(x)
print(ans)

