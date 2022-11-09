n=int(input())
l=[0,1,1]
a=1
b=2
for i in range(n):
    c=a+b
    l.append(c)
    a=b
    b=c
for i in range(n):
    if l[i]>n:
        r1=l[i-1]
        r2=l[i]
        break
if r1-n==n-r2:
    print(r1,r2)
elif n-r1>r2-n:
    print(r2)
else:
    print(r1)