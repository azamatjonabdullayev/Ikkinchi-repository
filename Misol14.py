from modullar import tengmi


son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
son3 = int(input("Uchinchi sonni kiriting: "))

a = tengmi(son1, son2, son3)

if a == True:
    print(f"Teng! ({a})")
else:
    print(f"Teng emas! ({a})")