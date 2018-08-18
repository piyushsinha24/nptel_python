m=int(input("enter m"))
n=int(input("enter n"))
for i in range(1,min(m,n)+1):
    if(m%i)==0 and (n%i)==0:
        mrcf=i                  #mrcf=most recent common factor
print(mrcf)
