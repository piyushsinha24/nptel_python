m=int(input("enter m"))
n=int(input("enter n"))
i=min(m,n)
while i>0:
    if(m%i)==0 and (n%i)==0:
       print(i)
       break
    else:
        i=i-1
