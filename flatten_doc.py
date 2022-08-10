l=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
i=0
while i<len(l):
    if type(l[i])==list:
        a=l[i]
        l.pop(i)
        j=0
        while j<len(a):
            l.insert(i+j,a[j])
            j=j+1
    else: i=i+1
print(l)
