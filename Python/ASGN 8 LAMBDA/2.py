# Q Sort all the characters of given string using lambda function

s='INDIA'

sort = ''.join(sorted(s, key=lambda x: x))

print(sort)