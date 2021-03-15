krumpli = float(input("Mennyi kg krumpli? "))
hagyma = float(input("Mennyi kg hagyma? "))
padlizsam = float(input("Mennyi kg padlizsam? "))
krumpliOsszeg = krumpli*70
hagymaOsszeg = hagyma *98
padlizsamOsszeg = padlizsam*200
print("Krumpli: ", krumpli,"kg  ",          "     *","           70Ft/kg    ",      "=   ",     krumpliOsszeg,"Ft")
print("Krumpli: ", hagyma,"kg ",          "      *","           98Ft/kg    ",      "=  ",      hagymaOsszeg,"Ft")
print("Krumpli: ", padlizsam,"kg",      "       *","          200Ft/kg    ",      "=  ",    padlizsamOsszeg,"Ft")
print("--------------------------------------------------------------------------")
print("Összesen: ","                                          ",krumpliOsszeg+hagymaOsszeg+padlizsamOsszeg, "Ft")