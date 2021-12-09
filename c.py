import re
from re import search

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

for m in re.finditer("[-, /, *, +]", value):
    print('match stack')
    #print('re.match', m)
    print('operator in regex version', m.group())
    print('operator', value[m.start()])
    print(m.start(0))
    #print(m.end(0))

#for o in operators:
    #m = patr.search(value).span()
    #if m:
        #m.span()
        #print(m)
        
        #print('m found')


for i in range(len(value)):
    #print(value[i])
    array.append(value[i])
    if value[i] == '*' or value[i] == '/' or value[i] == '+' or value[i] == '-' or value[i] == '^':
        if value[i] =='*': #or value[i] == '/':
            print('isMultiplication', i)
        elif value[i] == '/':
            print('isDivision', i)
        elif value[i] == '-':
            print('isSubstraction', i)
        elif value[i] == '+':
            print('isSum', i)
        elif value[i] == '^':
            print('isElev', i)




print(value[0:2])
print(array)
print(has_chars(value))