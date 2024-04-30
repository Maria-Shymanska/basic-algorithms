# Arrays

# We can create an array NumPy, use function numpy.array().

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: array([1, 2, 3, 4, 5])


arr = np.array([1, 2, 3, 4, 5])
print(arr + 2)  # Output: array([3, 4, 5, 6, 7])

# we can perform operations such as addition, substractions, multiplication between two arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr)) # Output: 15
print(np.mean(arr)) # Output: 3.0


# Lists
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))    # Output: 15
print(np.mean(arr))   # Output: 3.0

# Списки можуть бути розширені за допомогою методу append().

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)    # Output: [1, 2, 3, 4, 5, 6]

# Ми можемо вставити елемент на конкретну позицію за допомогою методу insert().

my_list = [1, 2, 3, 5]
my_list.insert(3, 4)  # Insert number 4 at position 3
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Ми можемо видалити елемент зі списку за допомогою методу remove() або pop().

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)  # Removes number 3 from the list
print(my_list)   # Output: [1, 2, 4, 5]

# Ми можемо відсортувати список за допомогою методу sort().

my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)   # Output: [1, 1, 2, 3, 4, 5, 9]

# Dictionaries  - це структури даних, засновані на принципі ключ-значення.

my_dict = {'name': 'John', 'age': 25}
print(my_dict)   # Output: {'name': 'John', 'age': 25}


# Ви можете отримати значення, пов'язане з конкретним ключем, використовуючи оператор [].

my_dict = {'name': 'John', 'age': 25}
print(my_dict['name'])  # Output: John

# Ви можете видалити пару ключ-значення зі словника, використовуючи оператор del.

my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 25}

# Sets - це структури даних, які використовуються для зберігання унікальних невпорядкованих елементів.

my_set = set([1, 2, 3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Елементи можна додати в множину за допомогою методу add().

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}


# Елементи можна видалити з множини за допомогою методів remove() або discard().

my_set = {1, 2, 3, 4, 5}
my_set.remove(1)
print(my_set)   # Output: {2, 3, 4, 5}


# можна виконувати математичні операції над множинами, такі як об'єднання (union),
# перетин (intersection), різниця (difference) та симетрична різниця (symmetric_difference).


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}


# Стек — це структура даних, у якій доступ до елементів обмежений таким чином, 
# що лише останній доданий елемент можна видалити
# (цей принцип називається LIFO — (Last In, First Out).

stack = []

# Щоб реалізувати операцію push, додавання елемента до стеку, ми можемо використати метод append(), 
# який буде додавати елементи на верхівку стеку.

stack.append('a')
stack.append('b')
stack.append('c')
print(stack)  # Output: ['a', 'b', 'c']

# метод pop() для видалення елемента з верхівки стеку.

print(stack.pop()) # Output: 'c'
print(stack)  # Output: ['a', 'b']

