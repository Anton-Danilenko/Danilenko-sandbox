s = input()
i = 0
cnt = 0
while i <= len(s) - 1:
    if len(s) == 1:
        print(s[i])
        break
    else:
        print(s[len(s) - 1 - cnt], sep='', end='')
        i += 1
        cnt += 1