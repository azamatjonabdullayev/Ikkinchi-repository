n = int(input("Listga nechta element kiritmoqchisiz?\n>>>>>>>>>> "))
list1 = list()
new = list()

while n > 0:
    son = int(input("Son kiriting: "))
    list1.append(son)
    n-=1


print(f"\nRo'yxat: {list1}")


for i in list1:
    if list1.count(i) > 1 and i not in new:
        new.append(i)

new.sort()

print(f"O'zgartirlgan ro'yxat: {new}")