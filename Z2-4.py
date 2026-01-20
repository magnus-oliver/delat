agilentCurrent_uA = 79.21

deltaCurrent_uA = 0.2*agilentCurrent_uA/100 + 0.003

print("För strömmen", agilentCurrent_uA, "är mätosäkerheten för y", deltaCurrent_uA, "mA.")

resistanceX = 254008.332

deltaResistance = resistanceX*((abs(4.497018/1000))+abs(deltaCurrent_uA/agilentCurrent_uA))

print(deltaResistance, "är deltaR för y")

