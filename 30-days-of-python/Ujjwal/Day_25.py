# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
t = int(input())

for i in range(t):
    n = int(input())
    f = 0
    if(n==0 or n==1):
        f = 1
    elif(n==2):
        f = 0
    else:
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if(n%i==0):
                f = 1
                break;
    if(f==0):
        print("Prime")
    else:
        print("Not prime")

