index=-1
def bsearch(seq,value,low,high):
    #searching for a value in a sorted seq[low:high]
    if(high-low == 0):
        return False
    mid = (high+low)//2
    if(seq[mid]== value):
        index=mid
        print("Found at "+str(index))
        return True
    if(seq[mid]>value):
        return bsearch(seq,value,low,mid)
    else:
        return bsearch(seq,value,mid+1,high)

seq=[1,4,5,6,8]
print(bsearch(seq,8,0,5))

        
        
        
    
