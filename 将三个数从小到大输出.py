def bubble(l):
    a=len(l)
    for i in range(0,a-1):
        for j in range(0,a-1-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
x=input()
y=input()
z=input()
l=[int(x),int(y),int(z)]
l=bubble(l)
print(l)
