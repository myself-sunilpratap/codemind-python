n=int(input())
l=[]
while n:
    l.append(n%10)
    n=n//10
print(max(l))    