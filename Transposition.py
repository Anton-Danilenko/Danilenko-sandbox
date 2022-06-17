a = [[1, 2, 4], [22, 55], [101, 223], [13, 5, 11]]
b = []
c = []
i = 0
j = 0
k = 0
while k <= len(a) - 1:
    b.insert(k, a[i][j])
    i += 1
    k += 1
k = 0
i = 0
j += 1
if j > len(a[i]) - 1:
    i += 1
    k += 1
while k <= len(a) - 1:
    if j > len(a[i]) - 1:
        i += 1
        k += 1
        if k > len(a) - 1:
            i = 0
    if j <= len(a[i]) - 1:
            c.insert(k, a[i][j])
            i += 1
            k += 1
            if k > len(a) - 1:
                j += 1
                k = 0
                i = 0
                if j == 2:
                    b = [b] + [c]
                else:
                    b.append(c)
                c = []
print(b)