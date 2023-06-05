def pal(n):
    return n==n[::-1]
a=input().lower().split()
c=0
for i in a:
    if (pal(i))==True:
        c+=1
print(c)        

