
l=[[1, 2], [3, 4], [5, 6, 7]]
l.reverse()
i=0
while i<len(l):
        a=l[i]
        a.reverse()
        l.pop(i)
        l.insert(i,a)
        i=i+1
print(l)