# Алгоритм із часовою складністю 
# 𝑂(1) — це константний час. Функція get_first_item просто повертає перше число списку.

def get_first_item(items):
    return items[0];
# Завжди виконується одна операція, незалежно від розміру списку

print(get_first_item([1, 2, 3, 4, 5]))


# Алгоритм із часовою складністю 𝑂(𝑛) просто проходить по списку чисел і друкує кожне число,
# а отже, кожне число у списку обробляється один раз.
# Тобто, якщо в нас є список з 10 числами, алгоритм виконає 10 операцій,
# а якщо список містить 1000 чисел — алгоритм виконає 1000 операцій.

def print_all_items(items):
  for item in items:
    print(item);
        
# Кількість операцій прямо пропорційна кількості елементів у списку

print_all_items([1, 2, 3, 4, 5])


# Прикладом алгоритму з часовою складністю 
# 𝑂(𝑛^2) може бути порівняння всіх пар векторів у списку, для перевірки того, чи є вони ортогональні. 
# Нагадаємо, що вектори вважаються ортогональними, якщо їх скалярний добуток дорівнює нулю. 


def dot_product(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))

def get_orthogonal_pairs(vectors):
  n = len(vectors)
  orthogonal_pairs = []
  
  for i in range(n):
    for j in range(i+1, n):
      if dot_product(vectors[i], vectors[j]) == 0:
        orthogonal_pairs.append((i, j))
        
  return orthogonal_pairs

vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
print(get_orthogonal_pairs(vectors))


