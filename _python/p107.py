def bubble_sort(lis):
    n = len(lis)
    for i in range(0,n - 1):
        sorted = True
        for j in range(0,n - i - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                sorted = False
        if sorted:
            break
    return lis

x = [6, 5, 4, 3, 2, 1, 4, 6, 4, 3, 24]

ans = bubble_sort(x)
print(ans)
