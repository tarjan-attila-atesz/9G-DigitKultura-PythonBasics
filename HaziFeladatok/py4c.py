import math
gombSugar = float(input("Add meg a gömb sugarát: "))
gombFelszin = 4 * math.pow(gombSugar, 2) * math.pi
gombTerfogat = (4 * math.pow(gombSugar, 3)* math.pi) / 3
print("A gömb felszíne: ", gombFelszin, ", a gömb térfogata: ", gombTerfogat)
