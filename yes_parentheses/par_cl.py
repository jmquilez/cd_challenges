# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from functools import total_ordering
import re
from re import search
import operator
import calculate
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


oParentheses = []
sect = []

for o in re.finditer("[)(]", value):
    #for s in re.finditer("[)]", value):
    oParentheses.append([o.start()])
    firstSection = value[o.start() + 1:len(value)]
    sect.append([firstSection, value[o.start()], o.start() + 1])
    #print("ese", o)
    #print("o", o)

example2 = re.search('geeks(?![a-z])', 'efgeeks123')
couples = []
openingBrackets = []
closingBrackets = []
opConmutate = []
clConmutate = []
sect0 = sect[0]
previousMatch = [sect0[1], sect0[2] - 1]
accumulativeMatches = []
unclosedOpenings = [sect0[2] - 1]
pairedOps = []

if sect0[1] == ")":
    print('sect_error:', sect)
    print(f"started with ')' at index: {sect0[2]}")
    raise ValueError("Cannot write enclosing bracket before opening bracket")


for s in sect:
    if s[1] == "(":
        openingBrackets.append(s[2] - 1)
    elif s[1] == ")":
        closingBrackets.append(s[2] - 1)




#483(((322323)))(322(32((328))

nuovoValor = None

indexAdvance = 0

inmutableVal = value

#483(((322323)))(322(32((328))

#algorithm destroyer
for l in openingBrackets:
    print("ELEI", l)
    print(value[l - 1:l])
    """print(value[:l])
    print(value[:l - 1])
    print(value[l:])
    print(value[l - 1:l])"""

    if re.match('(?=[0-9)(])', inmutableVal[l - 1:l]):
        print("mult omission founds")
        vsl = value[:l + indexAdvance]
        print(value[:l + indexAdvance])
        print(value[l + indexAdvance:])
        if vsl[-1] == "(":
            value = value[:l + indexAdvance] + "1" + "*" + value[l + indexAdvance:]
            indexAdvance+=2
        else:
            value = value[:l + indexAdvance] + "*" + value[l + indexAdvance:]
            indexAdvance+=1
        #value = value[:l + indexAdvance] + "*" + "(" + value[l + indexAdvance + 1:]
        
        print("THEvalue", value)

    """if re.search('(?<=[0-9)(])', value[:l + 1]):
        print("mult omission founds")
        value = value[:l] + "*" + "(" + value[l + 1:]
        print("newVal", value)"""
    #newStr = value[:s["begin"]] + str(res) + value[s["end"] + 1:]
    #if value[l - 1] != ""

print("finite VALUE:", value)

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
    sect.append([firstSection, value[o.start()], o.start() + 1])
    #print("ese", o)
    #print("o", o)


print('sect', sect)

example2 = re.search('geeks(?![a-z])', 'efgeeks123')
couples = []
openingBrackets = []
closingBrackets = []
opConmutate = []
clConmutate = []
sect0 = sect[0]
previousMatch = [sect0[1], sect0[2] - 1]
accumulativeMatches = []
unclosedOpenings = [sect0[2] - 1]
pairedOps = []

print("example2", example2.start())
print('unclosedOpenings_start', unclosedOpenings)

if sect0[1] == ")":
    print('sect_error:', sect)
    print(f"started with ')' at index: {sect0[2]}")
    raise ValueError("Cannot write enclosing bracket before opening bracket")


for s in sect:
    if s[1] == "(":
        openingBrackets.append(s[2] - 1)
    elif s[1] == ")":
        closingBrackets.append(s[2] - 1)

if len(closingBrackets) > len(openingBrackets):
    raise ValueError("You exceed the limit of closing parentheses")

for s in sect:

    if re.match('(?=[)(])', s[0]):
        s0 =s[0]
        pw = re.match('(?=[)(])', s0)
        if s0[pw.start()] == ")" and previousMatch[0] == "(":
            print('end with nothing inside brackets; previousMatch:', previousMatch)
            raise ValueError("You put nothing inside brackets within last previous match")

    if re.match('(?![\s\S])', s[0]):
        s0 = s[0]
        pw = re.match('(?![\s\S])', s0)
        print("unclosedOpenings before continue:", unclosedOpenings)
        print("last_unclosed", unclosedOpenings[-1])
        print("ese before continue:", s)
        if s[1] == ")" and len(unclosedOpenings) > 0:
            last = unclosedOpenings[-1]
            unclosedOpenings.pop(-1)
            isNested = False
            if len(unclosedOpenings) > 0:
                isNested = True
            pairedOps.append(last)
            couples.append([{
                "begin": last,
                "end": s[2] - 1,
                "isNested": isNested,
                "isNestedLinear": None
            }])
        print('continue')
        break

    if re.match('([)(])(?=[0-9-+/*^)(])', s[0]):
        s0 =s[0]
        pw = re.match('([)(])(?=[0-9-+/*^)(])', s0)
        print("foundItem at Index:", pw.start())
        print("item (CONSECUTIVE) is:", s0[pw.start()])
        print("s is:", s)
        if s0[pw.start()] == ")" and previousMatch[0] == "(":
            print('nothing inside brackets; previousMatch:', previousMatch)
            clConmutate.append(s[2] - 1)
            print(clConmutate)
            print("closing bracket CONSECUTIVE")
            raise ValueError("You put nothing inside brackets")
        elif s0[pw.start()] == "(":
            #accumulativeMatches.append([s0[pw.start()], s[2] + pw.start() + 1])
            #minusone = accumulativeMatches[-1]
            #if minusone
            unclosedOpenings.append(s[2] + pw.start())
            print('added to unclosedOpenings_NON_CONSECUTIVE', s[2] + pw.start() + 1)
            print('unclosedOpenings', unclosedOpenings)
            print('previousMatch', previousMatch)
            previousMatch = ["(", s[2] + pw.start()]
            #previousMatch = ["(", s0[pw.start()]]
            #previousMatch = ["(", s[2]]
            if len(accumulativeMatches) == 0:
                accumulativeMatches.append([s[1], s[2] - 1])
            if len(accumulativeMatches) > 0:
                minusone = accumulativeMatches[-1]
                if minusone[1] != s[2] - 1:
                    accumulativeMatches.append([s[1], s[2] - 1])
            
            accumulativeMatches.append([s0[pw.start()], s[2] + pw.start()])
            print('accumulativeMatches', accumulativeMatches)
            opConmutate.append(s[2] - 1)
            print(opConmutate)
            print("opening bracket CONSECUTIVE")
        elif s0[pw.start()] == ")":
            print('previousMatch', previousMatch)
            previousMatch = [")", s[2] + pw.start() + 1]
            if len(unclosedOpenings) > 0:
                last = unclosedOpenings[-1]
                unclosedOpenings.pop(-1)
                isNested = False
                if len(unclosedOpenings) > 0:
                    isNested = True

                pairedOps.append(last)
                couples.append([
                    {
                        "begin": last, 
                        "end": s[2] + pw.start(),
                        "isNested": isNested,
                        "isNestedLinear": None
                    }])
                
            else:
                raise ValueError("no opening bracket found. Too many closing brackets")
        """elif s0[pw.start()] == ")":
            if previousMatch[0] == "(":
                couples.append[previousMatch[1], s[2] + pw.start()]
                print('couple added CONSECUTIVE', couples)
            else:
                print('previousMatch', previousMatch)
                previousMatch = [")", s[2] + pw.start()]
                if len(accumulativeMatches) == 0:
                    accumulativeMatches.append([s[1], s[2] - 1])
                if len(accumulativeMatches) > 0:
                    minusone = accumulativeMatches[-1]
                    if minusone[1] != s[2] - 1:
                        accumulativeMatches.append([s[1], s[2] - 1])
            
                accumulativeMatches.append([s0[pw.start()], s[2] + pw.start()])
                print('accumulativeMatches', accumulativeMatches)
                opConmutate.append(s[2] - 1)
                print(opConmutate)
                print("closing bracket CONSECUTIVE")"""
        
    #make elif re.match('([0-9-+/*^]+)(?=[)(])', s[0]):        
    elif re.search('([0-9-+/*^])(?=[)(])', s[0]):
        s0 = s[0]
        pw = re.search('([0-9-+/*^])(?=[)(])', s0)
        print("foundItem at Index:", pw.start())
        print("item is:", s0[pw.start() + 1])
        print("s is:", s)
        if s0[pw.start() + 1] == ")":
            print('previousMatch', previousMatch)
            previousMatch = [")", s[2] + pw.start() + 1]
            if len(unclosedOpenings) > 0:
                last = unclosedOpenings[-1]
                unclosedOpenings.pop(-1)
                isNested = False
                if len(unclosedOpenings) > 0:
                    isNested = True

                pairedOps.append(last)
                couples.append([
                    {
                        "begin": last, 
                        "end": s[2] + pw.start() + 1,
                        "isNested": isNested,
                        "isNestedLinear": None
                    }])
                #couples.append([last, s[2] + pw.start() + 1])
                
            else:
                raise ValueError("no opening bracket found. Too many closing brackets")

            """if previousMatch[0] == "(":
                
                couples.append([previousMatch[1], s[2] + pw.start() + 1]) 
                print('couple added NON-CONSECUTIVE', couples)
                print('previousMatch', previousMatch)
                previousMatch = [")", s[2] + pw.start() + 1]
            else:
                print('previousMatch', previousMatch)
                previousMatch = [")", s[2] + pw.start() + 1]
                #previousMatch = [")", s0[pw.start()]]
                #previousMatch = [")", s[2]]
                clConmutate.append(s[2] - 1)
                print(clConmutate)
                print("closing bracket")"""
        elif s0[pw.start() + 1] == "(":
            print('previousMatch', previousMatch)
            previousMatch = ["(", s[2] + pw.start() + 1]
            unclosedOpenings.append(s[2] + pw.start() + 1)
            print('added to unclosedOpenings_NON_CONSECUTIVE', s[2] + pw.start() + 1)
            print('unclosedOpenings', unclosedOpenings)
            #previousMatch = ["(", s0[pw.start()]]
            #previousMatch = ["(", s[2]]
            opConmutate.append(s[2] - 1)
            print(opConmutate)
            print("opening bracket")
    #previousMatch = [s[1], s[2]]

print("total couples", couples)
print('opening brackets:', openingBrackets)
print('closing brackets:', closingBrackets)

nonPaired = []

for a in openingBrackets:
    #ol = pairedOps.index(a)
    try:
        ol = pairedOps.index(a)
        print("indexed", ol)
    except ValueError:
        nonPaired.append(a)
        print("OPENING NOT PAIRED", nonPaired)

nonPaired.sort(reverse=True)

print("sorted list:", nonPaired)

print("unclosedOpenings len:", len(unclosedOpenings))
for k in range(len(nonPaired)):
    s = nonPaired[k]
    isNested = False
    unclosedOpenings.pop(-1)
    print("longitud:", len(unclosedOpenings))
    print("current number", s)
    if len(unclosedOpenings) > 0:
        isNested = True
    couples.append([{
        "begin": s,
        "end": len(value),
        "isNested": isNested,
        "isNestedLinear": None
    }])
    value = value + ")"
    print("value_PAIRED", value)

print("complete_VALUE", value)
print("unclosedOpenings def length:", unclosedOpenings)
print("def couples", couples)

def srt(z):
    curr = z[0]
    return curr["begin"]

couples.sort(key=srt, reverse=False)
print("sorted couples", couples)

def srt2(z):
    return z["begin"]

nonNesteds = []
for c in couples:
    s = c[0]
    if s["isNested"] == False:
        print("NON_NESTED")
        nonNesteds.append(s)
        print("NON_NESTEDs value", nonNesteds)

print("total NON_NESTEDS", nonNesteds)
nonNesteds.sort(key=srt2, reverse=False)
print("total SORTED NON_NESTEDs", nonNesteds)

nestingGroups = []

i = 0
for g in nonNesteds:
    temp =  []
    for l in couples:
        o = l[0]
        if o["begin"] > g["begin"] and o["end"] < g["end"]:
            temp.append(o)
    nestingGroups.append(temp)
    i+=1

print("TOTAL NESTING GROUPS", nestingGroups)
print("NESTING GROUPS LENGTH", len(nestingGroups))
print("NON NESTEDS", nonNesteds)

"""pairedOpenings = []


for a in openingBrackets:
    for k in couples:
        p = k[0]
        if p["begin"] == a:
            pairedOpenings.append(a)
            print("found match, paired openings:s", pairedOpenings)"""


"""for c in couples:
    s = c[0]
    indx = openingBrackets.index(s["begin"])
    if (indx):"""



sc = couples[0]
print("scCouples", sc)
newStr = None
nesteds = 0

for c in couples:
    s = c[0]
    if s["isNested"] == True:
        print("neested")
        nesteds+=1
        print("nesteds value", nesteds)

inmutVal = value
totalSubstract = 0
"""for p in nestingGroups:
    print("Repeating nested loop")
    last = p[-1]
    print("lastGroup", last)
    #take "value[s["begin"] + 1:s["end"]]" from newStr instead, and change every time
    print("op to perform:", inmutVal[last["begin"] + 1:last["end"]])
    res = calculate.perform_operations(realPow, inmutVal[last["begin"] + 1:last["end"]])
    print("itWasNested")
    print(res)
    value = value[:last["begin"] + totalSubstract] + str(res) + value[last["end"] + totalSubstract + 1:]
    print("newVal", value)
    #newStr = value[:last["begin"] + totalSubstract] + str(res) + value[last["end"] + totalSubstract + 1:]
    #print("newString", newStr)
    p.pop(-1)
    #nesteds-=1
    print("nesteds current value (while) is", nesteds)
    totalSubstract-=2"""
n = 1
ad = 0
need = 0
frst = True
n1, n2 = 0, 1
count = 0
inmutLen = len(inmutVal)
totalSbs = 0

for p in nestingGroups:
    while len(p) > 0:
        print("starting correct")
        print("total Sbs", totalSbs)
        last = p[-1]
        print("lastGr", last)
        print("before sect VALUE", value[:last["begin"]])
        print("after sect VALUE", value[last["end"] + totalSbs+ 1:])
        rw_str = value[last["begin"] + 1:last["end"] + totalSbs]
        op_toPerform = ""
        if "(" in rw_str and ")" in rw_str:
            op_toPerform = rw_str.replace("(", '')
            op_toPerform = op_toPerform.replace(")", '')
        else:
            op_toPerform = rw_str
        
        print("op to perform:", op_toPerform)
        
        res = calculate.perform_operations(realPow, op_toPerform)
        
        res_len = len(str(res))

        print("value before part:", value[:last["begin"]])
        # + 2*ad
        print("value after part:", value[last["end"] + totalSubstract + 1:])

        value = value[:last["begin"]] + str(res) + value[last["end"] + totalSbs + 1:]

        print("new Value_", value)
        p.pop(-1)

        total_res_len = len(value)

        print("inmutValLen", inmutLen)
        print("total value len", total_res_len)


        totalSbs = 0
        totalSbs = -1*(inmutLen - total_res_len)


for p in nestingGroups:
    while len(p) > 0:
        print("starting equivocated")
        print("Repeating nested loop")
        last = p[-1]
        print("lastGroup", last)
        print("totalSUbstract", totalSubstract)
        print("before section INMUTABLE:", inmutVal[:last["begin"] + totalSubstract])
        print("after section INMUTABLE:", inmutVal[last["end"] + totalSubstract + 1:])
        print("ene value", n)
        print("ad value", ad)
        print("before section VALUE:", value[:last["begin"]])
        #+ 2*(n - 1)
        #2*ad +
        print("after section VALUE:", value[last["end"] + totalSubstract + 2*ad + 1:])
        #take "value[s["begin"] + 1:s["end"]]" from newStr instead, and change every time
        ##raw_string = inmutVal[last["begin"] + totalSubstract + 1:last["end"] + totalSubstract
        ####raw_string = inmutVal[last["begin"] + 1:last["end"] + totalSubstract]
        print("ending_value", value[:last["end"] + totalSubstract])
        print("index VALUE", last["end"] + totalSubstract + 1)
        print("index RAW STRING", last["end"] + totalSubstract)
        print("longitudinale", len(value[last["end"] + totalSubstract + 1:]))
        # + 2*ad
        raw_string = value[last["begin"] +  1:last["end"] + totalSubstract + 2*ad]
        print("raw_string:", raw_string)
        raw_str_len = len(raw_string) + 2*n
        print("raw_str_len", raw_str_len)

        op_toPerform = ""
        if "(" in raw_string and ")" in raw_string:
            op_toPerform = raw_string.replace("(", '')
            op_toPerform = op_toPerform.replace(")", '')
        else:
            op_toPerform = raw_string
        #print("op to perform:", inmutVal[last["begin"] + 1:last["end"]])
        print("op to perform:", op_toPerform)
        #res = calculate.perform_operations(realPow, value[last["begin"] + totalSubstract + 1:last["end"] + totalSubstract])
        res = calculate.perform_operations(realPow, op_toPerform)
        #res = calculate.perform_operations(realPow, inmutVal[last["begin"] + 1:last["end"]])
        res_len = len(str(res))
        diff = raw_str_len - res_len + 2*ad
        print("res_len", res_len)
        print("diff", diff)
        print("itWasNested")
        print("res:", res)
        print("total substract:", totalSubstract)
        ####print("value before part:", inmutVal[:last["begin"] + totalSubstract])
        ####print("value after part:", inmutVal[last["end"] + totalSubstract + 1:])
        ####value = inmutVal[:last["begin"] + totalSubstract] + str(res) + inmutVal[last["end"] + totalSubstract + 1:]
        print("totalVal", value)
        ####print("value before part:", value[:last["begin"] + totalSubstract])
        
        print("value before part:", value[:last["begin"]])
        # + 2*ad
        print("value after part:", value[last["end"] + totalSubstract + 1:])
        
        #value = inmutableVal[:last["begin"] + totalSubstract] + str(res) + inmutableVal[last["end"] + totalSubstract + 1:]
        ####value = value[:last["begin"] + totalSubstract] + str(res) + value[last["end"] + totalSubstract + 1:]
        ####value = value[:last["begin"]] + str(res) + value[last["end"] + totalSubstract + 2*(n - 1)  + 1:]
                                                                                      # + 2*ad 
        value = value[:last["begin"]] + str(res) + value[last["end"] + totalSubstract + 1:]
        print("current ad value:", ad)
        print("newVal", value)
        #newStr = value[:last["begin"] + totalSubstract] + str(res) + value[last["end"] + totalSubstract + 1:]
        #print("newString", newStr)
        p.pop(-1)
        """p[-1] = {
            "begin": 
        }"""
        #nesteds-=1
        print("nesteds current value (while) is", nesteds)
        #totalSubstract-=1
        totalSubstract-=diff
        print("substractAfterLoop", totalSubstract)
        n+=1
        if frst == True:
            need+=1
            frst = False
        elif need == 1: 
            need-=1
            ad+=1
        elif need == 0:
            need+=1
    print("cycle ended")

"""while nesteds > 0:
    for c in couples:#sc:
        s = c[0]
        if s["isNested"] == True:
            print('itIsNested')
            #take "value[s["begin"] + 1:s["end"]]" from newStr instead, and change every time
            res = calculate.perform_operations(realPow, value[s["begin"] + 1:s["end"]])
            print("itWasNested")
            print(res)
            newStr = value[:s["begin"]] + str(res) + value[s["end"] + 1:]
            print("newString", newStr)
            nesteds-=1
            print("nesteds current value (while) is", nesteds)
"""


"""if len(closingBrackets) > len(openingBrackets):
    raise ValueError("You exceed the limit of closing parentheses")"""
#print('opconmutate', opConmutate)
#print('clconmutate', clConmutate)
#43*(322(32*8/32^2^2*328))

"""for s in sect:
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
        print(s)"""
   
   
    
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

for s in sections:
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