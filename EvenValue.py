a = [1, 2, 4, 5, 12, 22, 32, 11, 44, 2, 4, 3, 1123212]
n = 0
#нахождение четных чисел
while (n < len(a) - 1):
    if a[n] % 2 == 0:
        print (a[n], end=',')
        n += 1
    else:
        n += 1
if n + 1 == len(a) and a[n] % 2 == 0:
    print(a[n])