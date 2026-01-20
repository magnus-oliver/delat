hpVoltage = 5.6237
deltaHP = hpVoltage*0.0035/100+0.0005*8/100
print("Mätosäkerhet spänning (mV):", deltaHP*1000)

agilentCurrent = 0.239
deltaAgilent = agilentCurrent*0.02/100+0.03
print("Mätosäkerhet ström (mA):", deltaAgilent)