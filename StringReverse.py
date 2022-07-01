print ("Введите строку")
s = input()
i = 0
cnt = 0
new = ""
while i <= len(s) - 1:
    if len(s) == 1:
        print(s[i])
        break
    else:
        new = new + s[len(s) - 1 - cnt]
        i += 1
        cnt += 1
print (new)