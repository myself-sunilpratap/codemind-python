l=input().split()
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if len(l[i])>len(l[j]):
            l[i],l[j]=l[j],l[i]
        elif len(l[i])==len(l[j]) and l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
for i in l:
    print(i,end=" ")