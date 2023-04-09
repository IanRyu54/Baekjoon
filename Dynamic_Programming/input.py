s = 'Do. Or do not. There is no try.'
print(len(s))
print(s.count('.'))
print(s.count(' '))
print(sum(1 for c in s if c.isupper()))
print(sum(1 for c in s if c.islower()))
print(sum([x.strip()[0].isupper() for x in s.split('.',2)]))
print(s.count('..'))
print(s)