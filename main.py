def calculate(s):
    if '+' in s or '-' in s or '*' in s or '/' in s:
        if '+' in s:
            return int(s[:s.find('+')]) + int(s[s.find('+') + 1:])
        elif '-' in s:
            return int(s[:s.find('-')]) - int(s[s.find('-') + 1:])
        elif '*' in s:
            return int(s[:s.find('*')]) * int(s[s.find('*') + 1:])
        else:
            return int(s[:s.find('/')]) / int(s[s.find('/') + 1:])
    else:
        return 'You need to sleep. I told you, that you need to use above mentioned characters by me.'


print('Enter your expression using "+", "-", "*" or "/".\n')
st = input()

print(calculate(st))
