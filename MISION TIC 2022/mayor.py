import os
os.system('cls')
n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n3 and n2 > n1:
    print(n2)
else:
    print(n3)