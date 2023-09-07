# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import randint

def queens() -> bool:
    coord_queens = _gen_queens()
    coord_queens_dict = {i: list(coord_queens[i]) for i in range(len(coord_queens))}

    count_row = count_col = count_diag = 0
    col_list = []
    row_list = []
    diag_list_col = []
    diag_list_row = []
    col_count_list = []
    row_count_list = []

    for key, item in coord_queens_dict.items():
        col_list.append(item[0])
        row_list.append(item[1])

    for i in col_list:
        col_count_list.append(col_list.count(i))
    col_set = set(col_count_list)

    for i in col_set:
        if i > 1:
            return False
        else:
            for i in row_list:
                row_count_list.append(row_list.count(i))
            row_set = set(row_count_list)
            for i in row_set:
                if i > 1:
                    return False
                else:
                    for value in coord_queens_dict.values():
                        diag_list_col.append(value[0])
                        diag_list_row.append(value[1])
                    diag_list_abs_col = []
                    for i in range(len(diag_list_col)):
                        for j in range(len(diag_list_col), i + 1, -1):
                            diag_list_abs_col.append(abs(diag_list_col[i] - diag_list_col[j - 1]))

                    diag_list_abs_row = []
                    for i in range(len(diag_list_row)):
                        for j in range(len(diag_list_row), i + 1, -1):
                            diag_list_abs_row.append(abs(diag_list_row[i] - diag_list_row[j - 1]))

                    for i in range(len(diag_list_abs_row)):
                        if diag_list_abs_col[i] == diag_list_abs_row[i]:
                            return False
    return True


def _gen_queens():
    queens = ((i + 1, randint(1, 9)) for i in range(8))
    return tuple(queens)


# coord_queens = ((1, 6), (2, 2), (3, 7), (4, 1), (5, 4), (6, 8), (7, 5), (8, 3))
# print(queens(coord_queens))
# coord_queens = ((1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4))
# print(queens(coord_queens))
# coord_queens = ((1, 3), (2, 5), (3, 2), (4, 8), (5, 1), (6, 7), (7, 4), (8, 6))
# print(queens(coord_queens))
# coord_queens = ((1, 2), (2, 6), (3, 8), (4, 3), (5, 1), (6, 4), (7, 7), (8, 5))
# print(queens(coord_queens))


print(_gen_queens())
print(queens())
print(_gen_queens())
print(queens())
