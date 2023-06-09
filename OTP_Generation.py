s=input()
g=''
for i in range(len(s)):
    if int(s[i])%2!=0:
        f=(int(s[i]))**2
        g=g+str(f)
print(g)        