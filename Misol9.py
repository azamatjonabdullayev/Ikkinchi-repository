n = int(input("Listga nechta element kiritmoqchisiz?\n>>>>>>>>>> "))
list1 = list()
new = list()

while n > 0:
    son = int(input("Son kiriting: "))
    list1.append(son)
    n-=1

print(f"Ro'yxat: {list1}")

for i in list1:
    if list1.count(i) == 1:
        new.append(i)

print(f"O'zgartirlgan ro'yxat: {new}")