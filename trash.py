import re
from re import search
import operator

value = input()

print(len(value))

array = []

def has_chars(input):
    chars = []
    nums = []
    for char in input:
        if char.isalpha():
            chars.append(char)
        elif char.isdigit():
            nums.append(char)
    
    total = []
    total.append(chars)
    total.append(nums)
    return total

re.compile(r"[a-zA-Z0-9]*")
#patrn = re.compile(value)



operators = ['/', '-', '+', '^']

regex = r'\d{2}'

patr = re.compile(regex)

x = re.findall("[-, /, *, +]", value)
y = re.search("[-, /, *, +]", value).span()
print('equis', x)
print('ygriega', y)

for m in re.finditer("[-, /, *, +, ^]", value):
    print('match stack')
    #print('re.match', m)
    print('operator in regex version', m.group())
    print('operator', value[m.start()])
    print('index', m.start(0))
    #print(m.end(0))