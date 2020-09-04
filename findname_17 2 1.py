#Напишите функцию find_name(), которая позволяет найти,
#в какой из трёх групп студентов чаще всего встречается человек с именем name = "Павел".

group_1 = "Антон Ярослав Ксения Мария Павел Егор Тимофей Павел".split()
group_2 = "Анастасия Анна Павел Егор Павел Арсений Антон Павел".split()
group_3 = "Татьяна Сергей Михаил Дмитрий Екатерина Полина".split()

def find_name(g):
    counter = {}
    name = "Павел"
    for name in g:
        counter[name] = counter.get(name, 0) + 1
    max_count = max(counter.values())
    most_frequent = [k for k, v in counter.items() if v == max_count]
    return max_count

print_gr = 0
count_gr = 0
for i in range(1):
    i = find_name(group_1)
    if i > count_gr:
        count_gr = i
        print_gr = group_1
    else:
        break
for i in range(1):
    i = find_name(group_2)
    if i > count_gr:
        count_gr = i
        print_gr = group_2
    else:
        break
for i in range(1):
    i = find_name(group_3)
    if i > count_gr:
        count_gr = i
        print_gr = group_3
    else:
        break
print(print_gr)