a = float(input("az oldal hossza: "))
b = float(input("az oldal hossza: "))
c = float(input("az oldal hossza: "))
if (a < (b+c) and b < (a+c) and c < (a+b)): 
    print("szerkeszthető")
else: 
    print("nem szerkeszthető")
exit()