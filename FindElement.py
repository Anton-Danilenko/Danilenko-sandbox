a = [1, 4, 'aa', 'Fds', 'F']
k = 0
#Найти F в массиве а
while k <= len(a) - 1:
    if a[k] == 'F':
        print (a[k])
        break
    else:
        k += 1
