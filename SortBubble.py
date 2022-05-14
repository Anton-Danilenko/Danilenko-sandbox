a = [-5, 22, 1, 0, 5]
n = 0
while (n < len(a) - 1):
    if a[n] > a[n + 1]:
        n = 0
        while (n < len(a) - 1):
            if a[n] > a[n + 1]:
                a.insert(n, a[n + 1])
                a.pop(n + 2)
            n += 1
        n = 0
    else:
        n += 1
print (a)
