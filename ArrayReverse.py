a = [1, 2, 'b', 12, 'AF', 542]
n = 0
b = []
b.append(a[len(a) - 1])
while n < len(a) - 1:
    n += 1
    b.append(a[len(a) - 1 - n])
print (b)
