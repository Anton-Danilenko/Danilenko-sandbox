print("Введите строку")
s = input()
print("Введите символ, который нужно удалить")
x = input()
new = ""
i = 0
cnt = 0
while i <= len(s) - 1:
    if s[i] != x:
        new = new + s[i]
        i += 1
    else:
        i += 1
print (new)