 #problem statement : to print the last value off fibunachi series foo the given lenght


lenght=int(input('enter the lenght series off own desire :'))
series=[0]
a,b=0,1
for i in range(lenght):
    a,b=b,a+b
    series.append(b)

lastval=series[(len(series)-1)]
print('the last value off the sires is ',lastval)