# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from functools import total_ordering
import re
from re import search
import operator
#from dotted_dict import DottedDict

realPow = int(input())
value = input()

op = {"+": operator.add, "-": operator.sub,
      "/": operator.truediv, "*": operator.mul, "^": operator.pow}


def needed_match(input, search=re.compile(r'[^0-9-+/*^)(]').search):
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

if re.search("[(]", value):
    z = re.findall("[(]", value)

print("zeta", z)

oParentheses = []
sect = []

for o in re.finditer("[)(]", value):
    #for s in re.finditer("[)]", value):
    oParentheses.append([o.start()])
    firstSection = value[o.start() + 1:len(value)]
    sect.append([firstSection, value[o.start()]])
    print("ese", o)
    print("o", o)

example2 = re.search('geeks(?![a-z])', 'efgeeks123')

print("example2", example2.start())   

for s in sect:
    if re.search('([0-9-+/*^])(?=[)(])', s[0]):
        s0 = s[0]
        pw = re.search('([0-9-+/*^])(?=[)(])', s0)
        print("foundItem at Index:", pw.start())
        print("item is:", s0[pw.start() + 1])
        print("s is:", s)
        if s0[pw.start() + 1] == ")":
            print("closing bracket")
        elif s0[pw.start() + 1] == "(":
           print("opening bracket")

for s in sect:
    if re.search('([0-9-+/*^])(?=[(])', s[0]):
        s0 = s[0]
        pe = re.search('([0-9-+/*^])(?=[(])', s0)
        both = re.search('([0-9-+/*^])(?=[)(])', s0)
        print("ok")
        print("opening ahead")
        print(pe.start())
        print(s)
    elif re.search('([0-9-+/*^])(?=[)])', s[0]):
        s0 = s[0]
        pe = re.search('([0-9-+/*^])(?=[(])', s0)
        print("closure ahead")
        print(pe.start())
        print(s)
   
   
    
print("sectsg", sect)
n = 0
for s in re.finditer("[)]", value):
    oParentheses[n].append(s.start())
    n+=1


print('oParentheses', oParentheses)
if re.search("[-, /, *, +, ^, ), (]", value):
    #x = re.findall("[-, /, *, +, ^, ), (]", value)
    x = re.findall("[-, /, *, +, ^]", value)
    y = re.search("[-, /, *, +, ^, ), (]", value).span()
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
            # n+=1
        else:
            print('i', i)
            print('n', n)
            print(m)
            if len(sections[n]) == 1:
                sections[n].append(m.start() - 1)
                sections.append([m.end()])
                n += 1
            elif len(sections[n]) > 1 or n in range(-len(sections), len(sections)):
                sections.append([m.start() - 1])
                n += 1
                #sections[n].append(m.start() - 1)

            print('even', sections)
        # n+=1
    elif i % 2 != 0:
        print('i', i)
        print('n', n)
        print(m)
        if len(sections[n]) == 1:
            sections[n].append(m.start() - 1)
            sections.append([m.end()])
            n += 1
        elif len(sections[n]) > 1 or n in range(-len(sections), len(sections)):
            sections.append([m.start() - 1])
            n += 1

        print('odd', sections)
        # n+=1
    i += 1
    # n+=1


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
l = 0

rango = len(sections) - 1

"""for u in range(len(sections) - 1):
    if x[u] == "^":
        print("pow")
        print("equisele", x[l])
        nexts = sections[l+1]
        #curr = sections[l]
        curr = sections[u]
        realchars.append(str(int(value[curr[0]:curr[1] + 1])**int(value[nexts[0]:nexts[1] + 1])))
        l+=1
        print("elepow", l)
        u+=1
    else:
        print("reg")
        #curr = sections[l]
        curr = sections[u]
        realchars.append(value[curr[0]:curr[1] + 1])
        l+=1
        print("ele", l)"""

for s in sections:

    """if x[l] == "^":
        nexts = sections[l + 1]
        realchars.append(value[s[0]:s[1] + 1]**value[nexts[0]:nexts[1] + 1])
    """
    realchars.append(value[s[0]:s[1]+1])
    l += 1

theRealChars = []
justPowed = 0
powerAde = [0, 0]

for i in range(len(realchars) - 1):
    if justPowed > 0 and x[i] != "^":
        print("skipping because justPowed")
        justPowed = 0
        print('currentop', x[i])
        print('theRealCharsProcessing', theRealChars)
    elif justPowed == 0 or x[i] == "^":
        if x[i] == "^" and justPowed == 0:
            if realPow == 1:
                poWed = int(realchars[i])**int(realchars[i+1])
                theRealChars.append(str(poWed))
                print('currentop', x[i])
                print('theRealCharsProcessing', theRealChars)
            elif realPow == 0:
                if i + 1 in range(-len(x), len(x)):
                    if x[i+1] == "^":
                        powerAde[0] = int(realchars[i])
                        powerAde[1] = int(realchars[i + 1])
                    else:
                        poWed = int(realchars[i])**int(realchars[i+1])
                        theRealChars.append(str(poWed))
                        print('realPow == 0, not advanced', poWed)
                        powerAde[0] = 0
                        powerAde[1] = 0
                else:
                    poWed = int(realchars[i])**int(realchars[i+1])
                    theRealChars.append(str(poWed))
                    print('realPow == 0, not advanced', poWed)
                    powerAde[0] = 0
                    powerAde[1] = 0

            justPowed += 1
        elif x[i] == "^" and justPowed > 0:
            if realPow == 1:
                poWed = int(theRealChars[-1])**int(realchars[i+1])
                theRealChars[-1] = poWed
                print('currentop', x[i])
                print('theRealCharsProcessing', theRealChars)
            elif realPow == 0:
                if i + 1 in range(-len(x), len(x)):
                    if x[i+1] == "^":
                        powerAde[1] = powerAde[1]**int(realchars[i+1])
                        #poWed = int(realchars[i - justPowed])**int(realchars[i+1])
                    else:
                        powerAde[1] = powerAde[1]**int(realchars[i+1])
                        powerAde[0] = powerAde[0]**powerAde[1]
                        theRealChars.append(str(powerAde[0]))
                        print('currentop', x[i])
                        print('powerAde == 0, ready to reset', powerAde)
                        powerAde[0] = 0
                        powerAde[1] = 0
                else:
                    powerAde[1] = powerAde[1]**int(realchars[i+1])
                    powerAde[0] = powerAde[0]**powerAde[1]
                    theRealChars.append(str(powerAde[0]))
                    print('currentop', x[i])
                    print('powerAde == 0, ready to reset', powerAde)
                    powerAde[0] = 0
                    powerAde[1] = 0

            justPowed += 1
        else:
            theRealChars.append(realchars[i])
            print('currentop', x[i])
            print('theRealCharsProcessing', theRealChars)

print('los caracteres reales', theRealChars)
xNoPowed = []

for s in x:
    if s == "^":
        print("its a pow")
    else:
        xNoPowed.append(s)

if x[-1] != "^":
    theRealChars.append(realchars[len(realchars) - 1])


print('xNoPowed', xNoPowed)
print("theRealOnes", theRealChars)
print("xNoPowed", xNoPowed)

total = 0
p = 0
o = -1
firstTime = True

comp = 0
firstTime0 = True
p0 = 0
o0 = -1

sums = []

addOrSub = []

for z in x:
    if z == "+" or z == "-":
        addOrSub.append(z)

for a in realchars:
    if firstTime:
        comp = int(realchars[0])
        firstTime = False
        sums.append({
            "total": realchars[0],
            "op": x[0],
            "indices": [0]
        })
        p0 += 1
        o0 += 1
    else:
        prevSum = sums[-1]
        if x[o0] == "*" or x[o0] == "/":
            if prevSum["op"] == "*" or prevSum["op"] == "/":
                prevIndices = prevSum["indices"]
                prevIndices.append(p0)
                sums[-1] = {
                    "total": op[x[o0]](float(prevSum["total"]),
                                       int(realchars[p0])),
                    "op": x[o0],
                    "indices": prevIndices
                }

            elif prevSum["op"] == "+" or prevSum["op"] == "-":
                sums[-1] = {
                    "total": op[x[o0]](float(realchars[o0]),
                                       int(realchars[p0])),
                    "op": x[o0],
                    "indices": [o0, p0]
                }
                """sums.append({
                "total": op[x[o0]](int(realchars[o0]),
                int(realchars[p0])),
                "op": x[o0],
                "indices": [o0, p0]
                })"""
            p0 += 1
            o0 += 1
        elif x[o0] == "+" or x[o0] == "-":
            sums.append({
                "total": float(realchars[p0]),
                "op": x[o0],
                "indices": [p0]
            })
            p0 += 1
            o0 += 1

addOrSubP = []
ftP = True
sumsP = []
pN = 0
oN = -1

for z in xNoPowed:
    if z == "+" or z == "-":
        addOrSubP.append(z)

if len(xNoPowed) > 0:
    for a in theRealChars:
        if ftP:
            comp = int(theRealChars[0])
            ftP = False
            sumsP.append({
                "total": theRealChars[0],
                "op": xNoPowed[0],
                "indices": [0]
            })
            pN += 1
            oN += 1
        else:
            prevSum = sumsP[-1]
            print("ene", oN)
            if oN in range(-len(xNoPowed), len(xNoPowed)):
                print("xnopowedoN", xNoPowed[oN])
                if xNoPowed[oN] == "*" or xNoPowed[oN] == "/":
                    if prevSum["op"] == "*" or prevSum["op"] == "/":
                        prevIndices = prevSum["indices"]
                        prevIndices.append(p0)
                        sumsP[-1] = {
                            "total": op[xNoPowed[oN]](float(prevSum["total"]),
                                                      int(theRealChars[pN])),
                            "op": xNoPowed[oN],
                            "indices": prevIndices
                        }

                    elif prevSum["op"] == "+" or prevSum["op"] == "-":
                        sumsP[-1] = {
                            "total": op[xNoPowed[oN]](float(theRealChars[oN]),
                                                      int(theRealChars[pN])),
                            "op": xNoPowed[oN],
                            "indices": [oN, pN]
                        }
                        """sums.append({
                        "total": op[x[o0]](int(realchars[o0]),
                        int(realchars[p0])),
                        "op": x[o0],
                        "indices": [o0, p0]
                        })"""
                    pN += 1
                    oN += 1
                elif xNoPowed[oN] == "+" or xNoPowed[oN] == "-":
                    sumsP.append({
                        "total": float(theRealChars[pN]),
                        "op": xNoPowed[oN],
                        "indices": [pN]
                    })
                    pN += 1
                    oN += 1


"""for a in realchars:
    if firstTime:
        total = int(realchars[0])
        firstTime = False
        p+=1
        o+=1
    else:
        total = op[x[o]](total, int(realchars[p]))
        p+=1
        o+=1"""

result = 0
ft = True
j = 0

"""for x in addOrSub:
    if ft == True:
        fir = sums[0]
        sec = sums[1]
        result = op[x](fir["total"], (sec["total"]))
        ft = False
        j+=1
    else:
        cons = sums[j + 1]
        result = op[x](result, cons["total"])
        j+=1
"""

resultNoPowed = 0
ft = True
j = 0

# 73*629^4*78-32^8/21*7432-454*73^12/432
# 1st sum: 891292074216414.0
# 2nd sum:

print('sumsP', sumsP)

if len(sumsP) > 0:
    for x in addOrSubP:

        if ft == True:
            fir = sumsP[0]
            sec = sumsP[1]

            resultNoPowed = op[x](fir["total"], (sec["total"]))
            print('resultNoPowedFirstTime', resultNoPowed)
            print('sumsP total', fir["total"], sec["total"])
            ft = False
            j += 1
        else:
            cons = sumsP[j + 1]
            resultNoPowed = op[x](resultNoPowed, cons["total"])
            print('sumsP total', cons["total"])
            print('resultNoPowed', resultNoPowed)
            j += 1
elif len(sumsP) == 0:
    print('len == 0')
    print(theRealChars[0])
    resultNoPowed = theRealChars[0]

# 54^2*632+87*5^3
# 65^2*732-76^2*64/2
print('longitud sumsP', len(sumsP))
if len(sumsP) == 1:
    one = sumsP[0]
    resultNoPowed = one["total"]

if len(sums) == 1:
    one = sums[0]
    result = one["total"]

print("special characters", x)
print("addOrSub", addOrSub)
print("sections", sections)
print("theReals", theRealChars)
print("realchars", realchars)
print("sums", sums)
print("resultNoPowed", resultNoPowed)
print("result", result)
print("total", total)
print("subNums", subNumbers)
print('arrayandIndexes', operArray)
print('lalongitud', len('34175792574734561318320347298712833833643272357706444319152665725155515612490248800367393390985216'))
