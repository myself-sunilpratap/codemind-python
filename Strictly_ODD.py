n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2!=0 and l[i]%2==0:
        print("False")
        break
else:
    print("True")