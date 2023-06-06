def h(n):
    s = set()
    while n != 1:
        if n in s:
            return False 
        s.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return True
num = int(input())
if h(num):
    print("True")
else:
    print("False")