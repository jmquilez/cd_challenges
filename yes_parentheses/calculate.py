from functools import total_ordering
import re
from re import search
import operator
import sre_constants

op = {"+": operator.add, "-": operator.sub,
      "/": operator.truediv, "*": operator.mul, "^": operator.pow}

def perform_operations(realPow, value):

    rgx_finditer = []
    spanes = []
    minus_set = []
    grps = []

    op = {"+": operator.add, "-": operator.sub,
      "/": operator.truediv, "*": operator.mul, "^": operator.pow}

    print("THIS IS THE VALUE MACABEIS:", value)

    newEquis = []
        #TODO: for g in x: newEquis.append({
        # "operator": "*",
        # "isAdjacent": false,
        # "index": 1
        # })

    if re.search("[-, /, *, +, ^, ), (]", value):
        #x = re.findall("[-, /, *, +, ^, ), (]", value)
        x = re.findall("[-, /, *, +, ^]", value)
        rgx = re.compile("[-, /, *, +, ^]")
        for m in rgx.finditer(value):
            newEquis.append({
                "operator": m.group(),
                "isAdjacent": False,
                "start": m.start(),
                "end": m.end()
            })
            rgx_finditer.append(m.start())
            spanes.append(m.span())
            grps.append(m.group())
            print("spanning", rgx_finditer)
        
        print("groupos", grps)
        print("spanes", spanes)
        print("total span", rgx_finditer)
        print("rgx", rgx.finditer(value))
        print("newEquis", newEquis)
        consecutives = []

        diferent = 0
        newLoop = True
        frst = True
        for h in range(len(newEquis) - 1):
            ls = h + diferent
            lo = h + diferent + 1
            ls1 = newEquis[ls]
            lo1 = newEquis[lo]
            print("ranging, ls:", ls)
            print("ranging, lo:", lo)
            print("newLoop", newLoop)
            if ls1["start"] == lo1["start"] - 1:
                print("found consecutive ones")
                skipin = False
                if frst == False:
                    for l in consecutives[-1]:
                        if newEquis[ls] == l:
                            print("skipin == True")
                            skipin = True
                if newLoop == True:
                    print("newLoop is true")
                    if skipin == False:
                        consecutives.append([newEquis[ls]])
                    consecutives[-1].append(newEquis[lo])
                    newLoop = False
                    print("consecs", consecutives)
                elif newLoop == False:
                    print("newLoop is false")
                    if skipin == False:
                        consecutives[-1].append(newEquis[ls])
                    consecutives[-1].append(newEquis[lo])
                    print("consecs", consecutives)
                    
                #diferent += 1
            else:
                print("newLoop else")
                newLoop = True
            frst = False
        print("consecutiveness", consecutives)

        aNew = True
        retraited = 0
        minsOrPlus = []
        lens = []

        for a in consecutives:
            a0 = a[0]
            if a0["operator"] == "-" or a0["operator"] == "+":
                print("found", a0["operator"], " in consecutives")
                #TODO: possible error
                for p in range(0, len(a) - 1):
                    curp = a[p]
                    if curp["operator"] == "*" or curp["operator"] == "/" or curp["operator"] == "^":
                        print("first case")
                        raise ValueError("Cannot", curp["operator"], " a", a0["operator"])
                    else:
                        opx = curp["operator"]
                        if aNew == True:
                            strp = opx + "1" #*
                            minsOrPlus.append([strp]) #opx
                            aNew = False
                            lens.append(-1*(len(a) - 1))
                        else:
                            strin = opx + "1" #*
                            minsOrPlus[-1].append(strin)
                        print("first case, its a:", curp["operator"])

            elif a0["operator"] == "*" or a0["operator"] == "/" or a0["operator"] == "^":
                print("found", a0["operator"], " in consecutives")
                for p in range(1, len(a)):
                    curp = a[p]
                    if curp["operator"] == "*" or curp["operator"] == "/" or curp["operator"] == "^":
                        print("second case")
                        raise ValueError("Cannot", curp["operator"], " a", a0["operator"])
                    else:
                        print("second case, its a:", curp["operator"])
                        opx = curp["operator"]
                        if aNew == True:
                            strp = opx + "1" #*
                            minsOrPlus.append([strp])
                            aNew = False
                        else:
                            strin = opx + "1" #*
                            minsOrPlus[-1].append(strin)
                        
            aNew = True
        

        print("minusOrPls", minsOrPlus)

        substrass = []

        for g in range(len(consecutives) - 1):
            try:
                i = consecutives[g]
                imens = i[-1]
                inext = consecutives[g + 1]
                inxs = inext[0]
                if inxs["operator"] == "*" or inxs["operator"] == "/" or inxs["operator"] == "^":
                    substr = value[imens["end"]:inxs["start"] + 1]
                else:
                    substr = value[imens["end"]:inxs["start"]]
                substrass.append(substr)
            except IndexError:
                print("haha didit")

        def lons():
            firstOfAll = consecutives[0]
            sero = firstOfAll[0]
            start = sero["start"]
            print("sero start", start)
            lastOfAll = consecutives[-1]
            last = lastOfAll[-1]
            lase = last["end"] + 1
            print("last end", lase)
            if sero["operator"] == "*" or sero["operator"] == "/" or sero["operator"] == "^":
                premiere = value[0:start + 1]
            else:
                premiere = value[0:start]
            print("premiere", premiere)
            seconde = value[lase:len(value)]
            print("seconde", seconde)
            substrass.insert(0, premiere)
            substrass.append(seconde)

        lons()
        print("substrass", substrass)

        origSubstrass = substrass

        for m in consecutives:
            m0= m[0]
            mlast = m[-1]
            values = [m0["start"], mlast["end"]]
            substr = value[values[0]:values[1]]
            #TODO: revise
            #substrass.append(substr)
        print("all substrass")

        totalSigns = []
        fst = True
        for c in minsOrPlus:
            print("new c")
            curVal = 0
            for h in range(len(c) - 1):
                try:
                    print("operating...")
                    curr = int(c[h])
                    nex = int(c[h + 1])
                    print("curr", curr)
                    print("nex", nex)
                    print("curVal", curVal)
                    if fst == True:
                        print("it is thefirst")
                        val = op["*"](curr, nex)
                        curVal = val
                        fst = False
                    else:
                        curVal = op["*"](curVal, nex)
                    
                except IndexError:
                    print("done it")
            fst = True
            totalSigns.append(curVal)

        defSigns = []
        for s in totalSigns:
            strin = str(s)
            if re.match("[-]", strin):
                mach =  re.match("[-]", strin)
                defSigns.append(mach.group())
            else:
                defSigns.append("+")

        print("signos totales", totalSigns)
        print("defSigns", defSigns)
        
        prevVal = ""
        first = True
        gx = 0
        specialIndices = []
        sechiones = []
        for i in defSigns:
            if first:
                prevVal = substrass[0] + i + substrass[1]
                print("value first", prevVal)
                specialIndices.append(len(substrass[0]))
                sechiones.append([0, len(substrass[0]) - 2])
                sechiones.append([len(substrass[0]), len(prevVal) - 2])
                first = False
            else:
                print("value next", prevVal)
                specialIndices.append(len(prevVal))
                prevLen = len(prevVal)
                prevVal = prevVal + i + substrass[gx + 1]
                sechiones.append([prevLen, len(prevVal) - 1])
            
            
            gx+=1

        if len(prevVal) > 0:
            value = prevVal
        
        findIters = []
        rel_sections = []
        
        for j in re.finditer("[-, /, *, +, ^]", value):
            findIters.append(j)

        print("findIters", findIters)
        frt = True
        justPass = False
        """for u in range(len(findIters) - 1):
            if frt:
                rel_sections.append([0, findIters[u].start() - 1])
                try:
                    if findIters[u].start() == findIters[u + 1].start() - 1:
                        print("justPass")
                        justPass = True
                except IndexError:
                    print("endeds")
                frt = False
            else:
                if justPass:
                    try:
                        print("computinh justPass")
                        rel_sections.append([findIters[u].start(), findIters[u + 1].start() - 1])
                        #if findIters[u].start() == findIters[u + 1].start() - 1:
                            #justPass = True
                        justPass = False
                    except IndexError:
                        print("indiced error")
                else:
                    try:
                        print("computing notPassed")
                        lastEnd = findIters[u - 1].end()
                        rel_sections.append([lastEnd, findIters[u].start() - 1])
                        if findIters[u].start() == findIters[u + 1].start() - 1:
                            print("justPass")
                            justPass = True
                    except IndexError:
                        print("excepted")"""

        for u in range(len(findIters)):
            print("current u", findIters[u].group())
            if frt:
                #rel_sections.append([findIters[u].end()])
                rel_sections.append([0, findIters[u].start() - 1])
                try:
                    if findIters[u].start() == findIters[u + 1].start() - 1:
                        "going to pass, first time"
                        #print("justPass")
                        #justPass = True
                    else:
                        print("first time")
                except IndexError:
                    print("endeds")
                frt = False
            else:
                try:
                    #sx = findIters[u + 1]
                    if findIters[u].start() - 1 == findIters[u - 1].start():
                        #rel_sections[u - 1].append(findIters[u].start())
                        #rel_sections.append([sx.start() - 1])
                        try:
                            rel_sections.append([findIters[u].start(), findIters[u + 1].start() - 1])
                            justPass = True
                            print("added to relsects")
                        except IndexError:
                            print("indiced badly")
                        
                    elif justPass:
                        print("cool")
                        justPass = False
                    else:
                        rel_sections.append([findIters[u - 1].end(), findIters[u].start() - 1])
                        print("regular")

                        
                except IndexError:
                    print("Index erros")
                    
                    
        def append_last():
            rel_sections.append([findIters[-1].start() + 1, len(value) - 1])
        append_last()
        
        #LAST WORKED HERE, TODO
        rel_x = []
        def real_x():
            for k in origSubstrass:
                print("sustraer", origSubstrass)
                print("ka", k)
                mats = re.findall("[-, /, *, +, ^]", k)
                s = 0
                print("mats", mats)
                for g in mats:
                    rel_x.append(g)
                    print("mateos", mats)
                    s+=1
                #rel_x.append(mats[0])
                #print("added", mats[0], " to rel_x")
        real_x()

        #if len(rel_x) > 0:
        x = rel_x
        
        #TODO:
        #x = rel_x
        #secciones = rel_sections
        #value = prevVal
        print("rel_x", rel_x)

        print("prevVal", prevVal)
        print("newVal", value)
        print("specialIndices", specialIndices)
        print("sechions", sechiones)
        print("REAL_SECCIONES", rel_sections)
        signatures = []
        valArr = []
        """for c in minsOrPlus:
            valToOp = ""
            for ñ in c:
                valToOp = valToOp + ñ
            valArr.append(valToOp)
            print("appended new valToOp")
            signatures.append(int(valToOp))"""

        print("valArr", valArr)
        print("signatures", signatures)
        popeados = 0
        ol = 0
        delta = 0
        differ = 0
        
        #TODO: ADD SIGNS IN CASE
        #remove
        for i in range(len(rgx_finditer) - 1):
            #if rgx_finditer[i + 1]:
            try:
                k = x[i + differ + 1]
                #s = grps[i + 1]
                if rgx_finditer[i + 1] == 1 + rgx_finditer[i]:
                    print("current i", i)
                    print("current indice", ol)
                    current = x[i + differ] # or ol instead of i
                    nexts = x[i + differ + 1]
                    current0 = rgx_finditer[i]
                    nexts0 = rgx_finditer[i + 1]
                    print("current0", current0)
                    print("nexts0", nexts0)
                    print("found consecutive operations at indexes:", rgx_finditer[i], rgx_finditer[i + 1])
                    print("operators are:", value[rgx_finditer[i]], value[rgx_finditer[i + 1]])
                    retr = []
                    retr.append(value[rgx_finditer[i + delta]])
                    retr.append(value[rgx_finditer[i + delta + 1]])
                    if (current == "-" or current == "+") and (nexts == "^" or nexts == "/" or nexts == "*"):
                        raise ValueError("cannot pow, divide or multiply inmediatly after a multiplication")
                        
                    print("grps ol", grps[ol])
                    print("grps ol + 1", grps[ol + 1])
                    sign = None

                    if (current == "-" or current == "+") and (nexts == "-" or nexts == "+"):
                        if (current == "-" and nexts == "+") or (current == "+" and nexts == "-"):
                            sign = "-"
                            
                        elif current == "+" and nexts == "+":
                            sign = "+"
                        elif current == "-" and nexts == "-":
                            sign = "+"
                        #op[x[o0]](float(prevSum["total"]),
                         #              int(realchars[p0]))
                    differ-=1
                    #append sign to newEquis or replace value in original x ==> newEquis.remove(ol), newEquis.remove(ol + 1). newEquis[ol] = sign 

                    #TODO (uncomment)
                    """if (current == "*" or current == "/" or current == "^") and (nexts == "-" or nexts == "+"):
                        print("conseq found")
                        if nexts == "+":
                            print("sum or subs encountered after operator:", current, "and it is:", nexts)
                            newEquis.pop(ol + differ + 1)
                            differ-=1
                        elif nexts == "-":
                            print("sum or subs encountered after operator:", current, "and it is:", nexts)
                            newEquis[ol + differ + 1] == {
                                "operator": "-",
                                "isAdjacent": True
                            }"""


                    if (grps[ol] == "-" or grps[ol] == "+") and (grps[ol + 1] == "-" or grps[ol + 1] == "+"):
                        #if (current == "-" and nexts == "+") or (current =="")
                        """mult = []
                        mult.push"""
                        if current == "-":
                            minus_set.append("-")
                            #x.pop(ol + popeados)
                            #value = value.replace(value[current + delta], "")
                            #value.pop(current + delta)
                            delta-=1
                            popeados-=1
                            print("popped minus, current x:", x)
                            print("current popeados (after):", popeados)
                            print("current minus_set", minus_set)
                        elif current == "+":
                            print("Plus encountered")
                            #x.pop(ol + popeados)
                            #value = value.replace(value[current + delta], "")
                            delta-=1
                            popeados-=1
                            print("popped plus, current x:", x)
                            print("current popeados (after):", popeados)

                    """for i in retr:
                        if i == "-":
                            minus_set.append(i)
                        elif i == "+":
                            print("Plus encountered")
                            x.pop(ol + popeados)
                            popeados-=1"""
                            #TODO: UNCOMMENT
                    """if (grps[ol] == "*" or grps[ol] == "/" or grps[ol] == "^") and (grps[ol + 1] == "-" or grps[ol + 1] == "+"):
                        print("found a consequence!!!")
                        
                        if grps[ol + 1] == "-":
                            minus_set.append("-")
                            print("o ele", ol)
                            print("popeados", popeados)
                            print(x[0])
                            x.pop(ol + popeados + 1)
                            #value = value.replace(value[current0 + delta + 1], "")
                            #value.pop(current + delta + 1)
                            delta-=1
                            popeados-=1
                            print("popped minus, current x:", x)
                            print("current popeados (after):", popeados)
                            print("current minus_set", minus_set)
                        elif grps[ol + 1] == "+":
                            print("Plus encountered")
                            x.pop(ol + popeados + 1)
                            #value = value.replace(value[current0 + delta + 1], "")
                            delta-=1
                            popeados-=1
                            print("popped plus, current x:", x)
                            print("current popeados (after):", popeados)
"""
                    
                    #if "+" in retr or "-" in retr:
                ol+=1
                    
                    #if (current == "*" and rgx_finditer[i + 1] == "/") or (rgx_finditer[i] == "*")

            except IndexError:
                print("already mapped")
                continue

        y = re.search("[-, /, *, +, ^, ), (]", value).span()
        print('equis', x)
        print('ygriega', y)
        print('minus set after', minus_set)
        print('equis after', x)
    else:
        print("literally NO OPERATIONS FOUND")
        return value

    #print("x span", x.span())
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

    #TODO: this changes everything
    #sections = sechiones
    if len(rel_sections) > 0:
            sections = rel_sections

    print("valor definitivo", value)
    print("secciones definitivas", sections)
    print("x definitiva", x)
    for s in sections:
        realchars.append(value[s[0]:s[1]+1])
        l += 1

    theRealChars = []
    justPowed = 0
    powerAde = [0, 0]
    print('valor_real', value)

    print("indices especials", specialIndices)

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
                    #TODO: change this to if "-" in
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
                            poWed = int(float(realchars[i]))**int(float(realchars[i+1]))
                            poWeRed = ""
                            if "-" in realchars[i]:
                                poWeRed = "-" + str(poWed)
                            else:
                                poWeRed = str(poWed)
                            theRealChars.append(poWeRed)
                            #theRealChars.append(str(poWed))
                            print('realPow == 0, not advanced', poWed)
                            powerAde[0] = 0
                            powerAde[1] = 0
                    else:
                        poWed = int(realchars[i])**int(realchars[i+1])
                        poWeRed = ""
                        if "-" in realchars[i]:
                            poWeRed = "-" + str(poWed)
                        else:
                            poWeRed = str(poWed)
                        theRealChars.append(poWeRed)
                        print('realPow == 0, not advanced', poWed)
                        powerAde[0] = 0
                        powerAde[1] = 0

                justPowed += 1
            elif x[i] == "^" and justPowed > 0:
                if realPow == 1:
                    poWed = int(theRealChars[-1])**int(realchars[i+1])
                    poWeRed = ""
                    if "-" in realchars[-1]:
                        poWeRed = "-" + str(poWed)
                    else:
                        poWeRed = str(poWed)
                    theRealChars[-1] = poWeRed
                    #theRealChars[-1] = poWed
                    print('currentop', x[i])
                    print('theRealCharsProcessing', theRealChars)
                elif realPow == 0:
                    if i + 1 in range(-len(x), len(x)):
                        if x[i+1] == "^":
                            if "-" in powerAde[1]:
                                powerAde[1] = -1*(powerAde[1]**int(realchars[i+1]))
                            else:
                                powerAde[1] = powerAde[1]**int(realchars[i+1])
                            #poWed = int(realchars[i - justPowed])**int(realchars[i+1])
                        else:
                            if "-" in powerAde[1]:
                                powerAde[1] = -1*(powerAde[1]**int(realchars[i+1]))
                            else:
                                powerAde[1] = powerAde[1]**int(realchars[i+1])
                            #powerAde[1] = powerAde[1]**int(realchars[i+1])
                            #powerAde[0] = powerAde[0]**powerAde[1]
                            poWeRed = ""
                            if "-" in powerAde[0]:
                                poWeRed = "-" + str(powerAde[0]**powerAde[1])
                            else:
                                poWeRed = str(powerAde[0]**powerAde[1])
                            theRealChars.append(poWeRed)
                            #theRealChars.append(str(powerAde[0]))
                            print('currentop', x[i])
                            print('powerAde == 0, ready to reset', powerAde)
                            powerAde[0] = 0
                            powerAde[1] = 0
                    else:
                        if "-" in powerAde[1]:
                            powerAde[1] = -1*(powerAde[1]**int(realchars[i+1]))
                        else:
                            powerAde[1] = powerAde[1]**int(realchars[i+1])
                        #powerAde[1] = powerAde[1]**int(realchars[i+1])
                        #powerAde[0] = powerAde[0]**powerAde[1]
                        poWeRed = ""
                        if "-" in powerAde[0]:
                            poWeRed = "-" + str(powerAde[0]**powerAde[1])
                        else:
                            poWeRed = str(powerAde[0]**powerAde[1])
                        theRealChars.append(poWeRed)
                        #theRealChars.append(str(powerAde[0]))
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
    const = 0
    for g in range(len(theRealChars) - 1):
        if theRealChars[g + const] == "":
            print("curr index", g + const)
            theRealChars.pop(g + const)
            const-=1
    """for g in theRealChars:
        if g == "":
            theRealChars.pop(const)
        const+=1"""

    local = 0
    print("real chars before", realchars)
    idx = 0
    for g in range(len(realchars) - 1):
        if realchars[g + local] == "":
            print("curr index", g + local)
            realchars.pop(g + local)
            local-=1
        #local-=1
        #local+=1

    """for g in realchars:
        if g == "":
            print("curr index", local)
            realchars.pop(local)
            local-=1
        #local-=1
        local+=1"""

    print('post-processed theReales', theRealChars)
    print('post-processed reales', realchars)
    xNoPowed = []

    
    for s in x:
        if s == "^":
            print("its a pow")
        else:
            xNoPowed.append(s)

    if x[-1] != "^":
        theRealChars.append(realchars[len(realchars) - 1])

    """curs = 0
    for s in x:
        if """

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

    print("theRealchars before loop", theRealChars)
    print("realchars before loop", realchars)
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
                    print("current_float_index", p0)
                    print("current_real_chars", realchars)
                    print("current_float", realchars[p0])
                    sums[-1] = {
                        "total": op[x[o0]](float(prevSum["total"]),
                                        int(float(realchars[p0]))),
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
                                                        int(float(theRealChars[pN]))),
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