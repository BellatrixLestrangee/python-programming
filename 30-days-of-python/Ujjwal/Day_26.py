    # Enter your code here. Read input from STDIN. Print output to STDOUT
i = list(map(int, input().split()))
a = list(map(int, input().split()))
f = 0
if(i[2]<a[2]):
    f = 0
elif(i[2]==a[2]):
    if(i[1]>a[1]):
        f = (i[1]-a[1])*500
    else:
        if(i[0]>a[0]):
            f = 15 * (i[0]-a[0])
        else:
            f = 0
else:
    f = 10000


    


print(f)
    
