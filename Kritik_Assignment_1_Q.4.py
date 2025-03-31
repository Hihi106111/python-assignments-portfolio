x = [-1,0,0.25,0.5,0.75,1]
o=0
while o<len(x):
    if 0<=x[o]<=1:
        a=0
        n=0
        while (x[o]**(2*n+1))/(2*n+1)>=0.0001:
            a+=((-1)**n)*(x[o]**(2*n+1))/((2*n)+1)
            n+=1
        else:
            n-=1
            if n<0:
                n=0
            error_bound = (x[o]**(2*n+1))/(2*n+1)
            print((a,n,error_bound))
    else:
        print("Error!")
    o+=1