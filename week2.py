def intreverse(n):
    rev=''
    while(n>0):
        rem=n%10
        rev=rev+str(rem)
        n=n//10
    return(rev)

def matched(s):
    substring1='('
    substring2=')'
    count1=s.count(substring1)
    count2=s.count(substring2)
    first_occurence1=s.find('(')
    first_occurence2=s.find(')')
    if s.startswith(')') or count1!=count2 or first_occurence2<first_occurence1 :
       return False
    else:
       return True

def isprime(r):
    if r > 1:
        c = 0
        if r == 2:
            return True
        for i in range(2, r):
            if r % i == 0:
                c = 1
                break
        if c == 1:
            return False
        else:
            return True
    else:
        return False

def sumprimes(l):
    s=0
    for i in l:
        if isprime(i) == True:
            s = s + i
    return s

 
        
        
