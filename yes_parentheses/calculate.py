from functools import total_ordering
import re
from re import search
import operator

op = {"+": operator.add, "-": operator.sub,
      "/": operator.truediv, "*": operator.mul, "^": operator.pow}

def perform_operations(realPow, value):

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

    for s in sections:
        realchars.append(value[s[0]:s[1]+1])
        l += 1

    theRealChars = []
    justPowed = 0
    powerAde = [0, 0]
    print('valor_real', value)

    print('secciones_reales', sections)

    print("caract_reales", realchars)

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

    result = 0
    ft = True
    j = 0

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

    """print("special characters", x)
    print("addOrSub", addOrSub)
    print("sections", sections)
    print("theReals", theRealChars)
    print("realchars", realchars)
    print("sums", sums)"""
    print("resultNoPowed", resultNoPowed)
    """print("result", result)
    print("total", total)
    print("subNums", subNumbers)
    print('arrayandIndexes', operArray)
    print('lalongitud', len('34175792574734561318320347298712833833643272357706444319152665725155515612490248800367393390985216'))"""
    return resultNoPowed