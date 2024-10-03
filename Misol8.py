a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new = list()

list1 = list()
list1.extend(a)
list1.extend(b)

for i in list1:
    if ((i in a and i not in b) or (i in b and i not in a)) and i not in new:
        new.append(i)

print(new)