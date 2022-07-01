print("Введите строку")
s = input()
print("Введите символ, который нужно удалить")
x = input()
i = 0
cnt = 0
while i <= len(s) - 1:
    if s[i] != x:
        print(s[i], sep='', end='')
        i += 1
    else:
        i += 1