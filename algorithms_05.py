# лінійний пошук
# Це найпростіший алгоритм пошуку, який використовується для знаходження певного елемента в списку (масиві).

def linear_reserch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
        return -1
    
numbers = [5, 10, 18, 4, 2]
print(linear_reserch(numbers, 7)) # output: -1



def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1

numbers = [1, 3, 5, 7, 9, 11]
print(linear_search(numbers, 7))  # Output: 3


def linear_search(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1

numbers = [1, 3, 5, 7, 9, 11]
print(linear_search(numbers, 7))  # Output: 3


# Двійковий (бінарний) пошук
# Це ефективний алгоритм пошуку, який працює на відсортованих списках (масивах).

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            return mid
 
    # якщо елемент не знайдений
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")

import matplotlib.pyplot as plt
import numpy as np

# Визначаємо кількість елементів та відповідні кроки для лінійного та двійкового пошуку
n = np.arange(1, 21)
linear_search_steps = n
binary_search_steps = np.log2(n)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(n, linear_search_steps, label='Linear Search', color='blue')
plt.plot(n, binary_search_steps, label='Binary Search', color='green')
plt.xlabel('Number of elements (n)')
plt.ylabel('Number of steps')
plt.title('Comparison of Linear and Binary Search')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Відображення графіка
plt.show()


# Індексно-послідовний пошук (Indexed Sequential Search) — це метод пошуку, який комбінує
# переваги послідовного та двійкового пошуку. 
# Цей алгоритм являє собою гібридний метод, який об'єднує в собі переваги послідовного та двійкового пошуку.
# переваги алгоритму:
# Ефективних для великих наборів даних
# Працює швидше ніж простий послідовний пошук
# Недоліки:
# Потребує додаткової пам'яті для індексної таблиці.
# Індексна таблиця повинна бути оновлена при зміні основного масиву.

# Створення індексної таблиці
def create_index_table(array, step):
    index_table = []
    for i in range(0, len(array), step):
        index_table.append((array[i], i))
        return index_table
    
# Основний відсортований масив
main_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

# створення індексованщї таблиці з кроком 4
index_table = create_index_table(main_array, 4)






