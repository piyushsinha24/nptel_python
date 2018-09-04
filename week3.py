def descending(l1):
    l2=sorted(l1,reverse=True)
    if(l1==l2):
        return True
    else:
        return False


def valley(l1):
  if(len(l1)==0):
    return(True)
  if(len(l1)==1):
    return(False)
  if(l1[0]<l1[1]):
    return(False)
  for i in range(0,len(l1)-1):
    if(l1[i]<l1[i+1]):
      pos=i
      break
    if(l1[i]==l1[i+1]):
      return(False) 
  else:
    return(False)
  for i in range(pos,len(l1)-1):
    if(l1[i]>=l1[i+1]):
      return(False)
  return(True)


def transpose(l):
    l2=[]
    res = [[l[j][i] for j in range(len(l))] for i in range(len(l[0]))]
    for row in res:
        l2.append(row)
    return l2
