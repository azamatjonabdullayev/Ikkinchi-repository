def birinchi_topshiriq():
    list1=[1, 2, 3]
    list2=[11, 22, 33]
    new_list = list()


    a = 0

    for i in list1:
        new_list.append(i)

        if a < len(list2):
            new_list.append(list2[a])
            a += 1


    print(new_list)


def ikkinchi_toshiriq():
    list1=[1, 2, 3, 4, 5]
    list2=[11, 22, 33]
    new_list = list()

    a = 0

    for i in list1:
        new_list.append(i)
    
        if a < len(list2):
            new_list.append(list2[a])
            a += 1

    print(new_list)


def uchunchi_topshiriq():
    list1=[1, 2]
    list2=[11, 22, 33, 44, 55]
    new_list = list()

    a = 0

    for i in list2:
        if a < len(list1):
            new_list.append(list1[a])
            a += 1
    
        new_list.append(i)

    print(new_list)


def yigindi(son: int):
    s = 0
    for i in range(1, son+1):
        s += i
    
    return s


def faktorial(son: int):
    
    if son == 0:
        return 1
    else:
        f = 1
        for i in range(1, son+1):
            f *= i
    
    return f


def tengmi(a: int, b: int, c: int):
    if a + b == c:
        return 1
    else:
        return 0


def juft_toq(son: int):
    if son % 2 == 0:
        return True
    else:
        return False


def ikkilik(son: int):
    return bin(son)[2:]