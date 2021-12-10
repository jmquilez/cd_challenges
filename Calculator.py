'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from functools import total_ordering
import re
from re import search
import operator
#from dotted_dict import DottedDict

value = input()

op = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul, "^": operator.pow }

def needed_match(input, search=re.compile(r'[^0-9-+/*^]').search):
    return not bool(search(input))

if needed_match(value) == False:
    raise ValueError("Input may only contain numbers and operators")

print(needed_match(value))

print(len(value))


def has_chars():
    return bool(re.search(r'\d'))

operators = ['/', '-', '+', '^']

regex = r'\d{2}'

x = []

patr = re.compile(regex)

if re.search("[-, /, *, +, ^]", value):
    x = re.findall("[-, /, *, +, ^]", value)
    y = re.search("[-, /, *, +, ^]", value).span()
    print('equis', x)
    print('ygriega', y)



operArray = []
subNumbers = []
sections = []
emes = []

i = 0
n = 0

print('ITERACIÓN')
print(re.finditer("[-, /, *, +, ^]", value))

for m in re.finditer("[-, /, *, +, ^]", value):
    if i % 2 == 0:
        if n == 0:
            sections.append([m.end()])
            print('i', i)
            print('n', n)
            print(m)
            print('even, 0', sections)
            #n+=1
        else:
            print('i', i)
            print('n', n)
            print(m)
            if len(sections[n]) == 1:
                sections[n].append(m.start() - 1)
                sections.append([m.end()])
                n+=1
            elif len(sections[n]) > 1 or n in range(-len(sections), len(sections)):
                sections.append([m.start() - 1])
                n+=1
                #sections[n].append(m.start() - 1)
           
            print('even', sections)
        #n+=1
    elif i % 2 != 0:
        print('i', i)
        print('n', n)
        print(m)
        if len(sections[n]) == 1:
            sections[n].append(m.start() - 1)
            sections.append([m.end()])
            n+=1
        elif len(sections[n]) > 1 or n in range(-len(sections), len(sections)):
            sections.append([m.start() - 1])
            n+=1
        
        print('odd', sections)
        #n+=1
    i+=1
    #n+=1


firstIndex = sections[0]

if firstIndex[0] != 0:
    sections.insert(0, [0, firstIndex[0] - 2])

if len(sections[len(sections) - 1]) == 1:
    sections[len(sections) - 1].append(len(value) - 1)

lastOne = sections[len(sections) - 1]

if lastOne[1] != len(value) - 1:
    sections.append([lastOne[-1] + 2, len(value) - 1])

print('OPERARRAY:')
for s in operArray:
    print('index', s['index'])
    print('char', s['char'])

realchars = []

for s in sections:
    realchars.append(value[s[0]:s[1]+1])

total = 0
p = 0
o = -1
firstTime = True
for a in realchars:
    if firstTime:
        total = int(realchars[0])
        firstTime = False
        p+=1
        o+=1
    else:
        total = op[x[o]](total, int(realchars[p]))
        p+=1
        o+=1

print("special characters", x)
print("sections", sections)
print("realchars", realchars)
print("total", total)
print("subNums", subNumbers)
print('arrayandIndexes', operArray)
