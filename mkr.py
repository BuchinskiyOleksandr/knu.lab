
def sort_columns(matrix):
    # Знаходимо суму елементів у кожному стовпці
    column_sums = [sum(column) for column in zip(*matrix)]
    # Сортуємо стовпці за зростанням
    sorted_columns = [column for _, column in sorted(zip(column_sums, zip(*matrix)))]
    # Перетворюємо список кортежів у список списків
    sorted_matrix = [list(row) for row in zip(*sorted_columns)]
    return sorted_matrix

# Приклад використання
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sorted_matrix = sort_columns(matrix)
print(sorted_matrix)