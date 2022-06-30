s = input()
i = 0
cnt = 1
while i <= len(s) - 1:
    if len(s) == 1:
        print('"', s[i], '"', ":", cnt, sep='', end=', ')
        break
    elif s[i] != s[i + 1]:
        cnt = 1
        if i == 0 or s[i] != s[i - 1]:
            print('"', s[i], '"', ":",  cnt, sep='', end=', ')
        i += 1
        if i == len(s) - 1:
            print('"', s[i], '"', ":",  cnt, sep='', end='')
            break
    else:
        while s[i] == s[i + 1]:
            cnt += 1
            i += 1
            if i == len(s) - 1:
                print('"', s[i], '"', ":",  cnt, sep='', end=', ')
                break
        if i == len(s) - 1:
            break
        print('"', s[i], '"', ":",  cnt, sep='', end=', ')
    continue