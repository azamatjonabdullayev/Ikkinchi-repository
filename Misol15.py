from modullar import juft_toq

son = int(input("Son kiriting: "))

a = juft_toq(son)

if a == 1:
    print(f"Kiritgan {son} soningiz juft son.")
elif a == 0:
    print(f"Kiritgan {son} soningiz toq son.")