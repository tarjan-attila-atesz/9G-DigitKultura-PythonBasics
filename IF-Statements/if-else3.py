# Bekérünk három számot
number1 = int(input("Írd ide az első számot: "))
number2 = int(input("Írd ide az második számot: "))
number3 = int(input("Írd ide az harmadik számot: "))

# feltételezzük, hogy az első számunk a nagyobb
largest_number = number1

# ellenőrizzük, hogy az másodjára bevitt szám tényleg nagyobb e, ha nem cseréljük
if number2 > largest_number:
    largest_number = number2

# ellenőrizzük, hogy a harmadjára bevitt szám tényleg nagyobb e, ha nem cseréljük
if number3 > largest_number:
    largest_number = number3

# Kiíratjuk az eredményt
print("A nagyobb számom a :", largest_number)
