z=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
l=[i for i in a if i not in b]
l=l+[i for i in b if i not in a]
for i in l:
    print(i,end=" ")