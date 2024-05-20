'''Функції для роботи з купами
Модуль heapq у Python надає функції для роботи з купами
Python надає вбудовану функцію heapify тільки для мінімальних куп, 
але ви можете легко створити максимальну купу для числових значень, помноживши кожне значення на -1.
Отже, функція heapify перетворює ітерабельний об'єкт у купу.'''

import heapq

nums = [4, 10, 3, 5, 1]
heapq.heapify(nums)
print(nums)  # Output: [1, 4, 3, 5, 10]


# Функція heappush(heap, elem) додає елемент до купи та перебудовує купу.
heapq.heappush(nums, 0)
print(nums)  # Output: [0, 4, 1, 5, 10, 3]

# Функція heappop(heap) видаляє та повертає найменший елемент із купи.
min_elem = heapq.heappop(nums)
print(min_elem)  # Output: 0
print(nums)  # Output: [1, 4, 3, 5, 10]


# Функція heappushpop(heap, elem) додає елемент до купи, а потім видаляє та повертає найменший елемент.
min_elem = heapq.heappushpop(nums, 2)
print(min_elem)  # Output: 1
print(nums)  # Output: [2, 4, 3, 5, 10]


# Функція heapreplace(heap, elem) видаляє та повертає найменший елемент, а потім додає новий елемент.
min_elem = heapq.heapreplace(nums, 0)
print(min_elem)  # Output: 2
print(nums)  # Output: [0, 4, 3, 5, 10]


# Функції nlargest(n, iterable, key=None) і nsmallest(n, iterable, key=None)
# повертають n найбільших та n найменших елементів з ітерабельного об'єкта відповідно.
largest_three = heapq.nlargest(3, nums)
smallest_three = heapq.nsmallest(3, nums)
print(largest_three)  # Output: [10, 5, 4]
print(smallest_three)  # Output: [0, 3, 4]
print(nums)  # [0, 4, 3, 5, 10]


# Один із популярних способів реалізації черги з пріоритетами — за допомогою купи (heap).
def convert_image(file_name, target_format):
    # Припустимо, що ця функція конвертує зображення (тут просто імітація)
    print(f"Конвертація {file_name} до {target_format} формату...")
    return f"{file_name.split('.')[0]}.{target_format}"

# Реалізація самої черги з пріоритетом
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (-priority, task))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return not bool(self.queue)
