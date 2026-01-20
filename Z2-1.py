flukeResults = [] # era värden för fluke här
flukeDelta = []

for i in flukeResults:
    deltaU = i*0.4/100+0.01
    flukeDelta.append(deltaU)

print("10 V ger för Fluke:", float(flukeDelta[0]*1000))
print("20 V ger för Fluke:", float(flukeDelta[1]*1000))
print("30 V ger för Fluke:", float(flukeDelta[2]*1000))

agilentResults = [] # era värden för agilent här
agilentDelta = []

for i in agilentResults:
    deltaAgilent = i*0.05/100+0.002
    agilentDelta.append(deltaAgilent)

print("10 V ger för Agilent:", float(agilentDelta[0]*1000), "mV")
print("20 V ger för Agilent:", float(agilentDelta[1]*1000), "mV")
print("30 V ger för Agilent:", float(agilentDelta[2]*1000), "mV")

hpResult = [] # era värden för HP här
hpDelta = []

for i in hpResult:
    if i < 15:
        deltaHP = i*0.0035/100+0.0005/10
        hpDelta.append(deltaHP)
    else:
        deltaHP = i*0.0045/100+0.0006
        hpDelta.append(deltaHP)

print("HP: 10 V ger:", float(hpDelta[0]*1000))
print("HP: 20 V ger:", float(hpDelta[1]*1000))
print("HP: 30 V ger:", float(hpDelta[2]*1000))