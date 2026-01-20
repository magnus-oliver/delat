hpVoltage = 5.6237 # ersätt med ert mätvärde
deltaHP = hpVoltage*0.0035/100+0.0005*8/100
print("Mätosäkerhet spänning (mV):", deltaHP*1000)

agilentCurrent = 0.239 # ersätt med ert mätvärde
deltaAgilent = agilentCurrent*0.02/100+0.03
print("Mätosäkerhet ström (mA):", deltaAgilent)