first_list = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
a_list = list()
d_list = list()
w_list = list()


for i in first_list:
    if i[0] == 'a':
        a_list.append(i)
    elif i[0] == 'd':
        d_list.append(i)
    elif i[0] == 'w':
        w_list.append(i)

print(a_list)
print(d_list)
print(w_list)