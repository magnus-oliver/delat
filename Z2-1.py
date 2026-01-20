flukeResults = [10.10, 20.08, 30.09]
flukeDelta = []

for i in flukeResults:
    deltaU = i*0.4/100+0.01
    flukeDelta.append(deltaU)

print("10 V ger:", float(flukeDelta[0]*1000))
print("20 V ger:", float(flukeDelta[1]*1000))
print("30 V ger:", float(flukeDelta[2]*1000))

hpResult = [10.126, 20.134, 30.080]
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