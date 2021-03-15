
number1 = int(input("Írd ide az első számot: "))
number2 = int(input("Írd ide az második számot: "))
number3 = int(input("Írd ide az harmadik számot: "))


largest_number = number1

if number2 > largest_number:
    largest_number = number2


if number3 > largest_number:
    largest_number = number3


print("A nagyobb számom a :", largest_number)
