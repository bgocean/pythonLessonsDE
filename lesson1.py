# v_list = list()
v_list = [1, 2, 3, 4, 5.1, 'some string']
v_list2 = [10, 20, 30]
# print(v_list)

cor = (1, 2, 3, 4, 5.1, 'some string', 10, 20, 30)
print(cor)
print(cor[5])

print(v_list2)
print(v_list[::2])  # срез

v_list2.append('привет!')
print(v_list2)

# v_list.extend(v_list2)
# print(v_list)

v_list2.clear()
print(v_list2)

v_list.pop(5)
print(v_list)
v_list.reverse()
print(v_list)

v_list3 = [1, 2, 3, 4, 5.1, 'some string', 1, 2, 3]
mult = set(v_list3)  #set - множество включает только уникальные элементы
print(mult)

f_mult = frozenset(v_list3) #замороженное множество не изменяется, как и кортэж
print(f_mult)