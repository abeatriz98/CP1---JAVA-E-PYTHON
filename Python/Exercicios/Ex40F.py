a = 1
b = 1
c = 1

for i in range (1, 21,1):
    f = a+b+c
    c = b
    b = a
    a = f
    print(f)
