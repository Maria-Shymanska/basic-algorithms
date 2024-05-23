# Лінійне програмування
# Симплекс метод
import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Визначення змінних
A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту А
B = pulp.LpVariable('B', lowBound=0, upBound=10, cat='Integer')  # Кількість продукту Б

# Функція цілі (Максимізація прибутку)
model += 50 * A + 40 * B, "Profit"

# Додавання обмежень
model += 5 * A + 2 * B <= 80  # Обмеження для машини №1
model += 3 * A + 2 * B <= 40  # Обмеження для машини №2

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробляти продуктів А:", A.varValue)  # 0.8
print("Виробляти продуктів Б:", B.varValue)  # 0.8


# Рандомізовані алгоритми 
# Тест Рабіна-Міллера є основою для багатьох криптографічних алгоритмів і систем, 
# де потрібно швидко знаходити великі прості числа.

import random

def is_prime(n, k=5):  # k - кількість ітерацій
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Знаходимо r та d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Проводимо k тестів
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Приклад використання:
n = 561  # Число Кармайкла
print(is_prime(n))  # поверне False, хоча 561 - псевдопросте число


# Універсальне хешування 

import random

class UniversalHash:
    def __init__(self, m, max_key):
        self.m = m
        self.p = self._next_prime(max_key)
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _next_prime(self, n):
        while True:
            n += 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                return n

    def hash(self, key):
        return ((self.a * key + self.b) % self.p) % self.m

# Приклад використання:
hasher = UniversalHash(100, 1000)
print(hasher.hash(123))
print(hasher.hash(456))


# Метод Монте-Карло 

import random

# Розміри прямокутника
a = 10  # ширина прямокутника
b = 5  # висота прямокутника

def is_inside(a, b, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    return y <= (b / a) * x

# Генерація випадкових точок
points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]

# Відбір точок, що знаходяться всередині трикутника
inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

# Кількість усіх точок та точок всередині
N = len(points)
M = len(inside_points)

# Теоретична площа трикутника та площа, обчислена методом Монте-Карло
S = (a * b) / 2  # Теоретична площа
Sm = (M / N) * (a * b)  # Площа за методом Монте-Карло

# Виведення результатів
print(f"Кількість точок всередині трикутника: {M}, загальна кількість точок: {N}")
print(f"Теоретична площа трикутника: {S}, площа за методом Монте-Карло: {Sm}")
