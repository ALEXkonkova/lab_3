# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, sep=','):
    list_str1 = str1.split(sep)
    list_str2 = str2.split(sep)
    i_list = list(set(list_str1).intersection(list_str2))
    i_list.sort()
    return i_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print(participants)