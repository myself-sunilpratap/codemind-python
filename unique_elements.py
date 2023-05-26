n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a:
        print(i,'',end='')
        a.append(i)