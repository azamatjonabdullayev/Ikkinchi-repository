list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
list2 = list()

for i in list1:    
    if i not in list2:
        list2.append(i)

print(list2)