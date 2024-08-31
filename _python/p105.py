

def binary_search(search_list,element):
    left,right=0,len(search_list)-1
    result=0

    while left<=right:
        mid=(left+right)//2
        if search_list[mid]==mid:
            result=mid
            return result
            break
        elif search_list[mid]<element:
            left=mid-1
        else:
            right=mid-1
    
    return -1


sorted_list=list(range(0,100))
target=20

x=binary_search(sorted_list,target)
print(sorted_list[x])
    