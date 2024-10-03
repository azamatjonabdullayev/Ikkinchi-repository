list1 = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9 , 7, 1]
list2 = list()
list3 = list()


for i in list1:
    if i !=0:
        list2.append(i)
    else:
        list3.append(i)

list2 += list3

print(list2)