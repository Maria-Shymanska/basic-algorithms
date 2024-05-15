'''Списки суміжності -  це структура даних, яка зберігає список вершин, з якими пов'язана кожна вершина. 
# Список суміжності для цього графа можна представити у форматі словника:'''

adj_list = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

print(adj_list)


'''Циклічний граф - характеризується наявністю одного або більше циклів, тобто шляхів,
# які починаються та закінчуються в одній i тій самій вершині. 
# Це основна відмінність циклічних графів від ациклічних графів, які не містять жодного циклу.'''

cyclic_graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

print(cyclic_graph)


'''Алгоритм DFS (глибина) починається з вибраної вершини та продовжує відвідування наступної необхідної вершини, 
що є сусідом попередньої, переходячи все глибше у граф,
доки не дійде до мертвого кінця, після чого він повертається назад,
щоб знайти необхідні вершини, які ще не були відвідані, і продовжує цей процес, поки не відвідає всі вершини.
Алгоритм DFS можна реалізувати в рекурсивному або ітеративному варіанті.'''


# Рекурсивна реалізація алгоритму

def dfs_recursive(grath, vertex, visited=None):
    if visited is None:
        visited  = set()
    visited.add(vertex)
    print(vertex, end = ' ')    # Відвідуємо вершину
    for neighbor in grath[vertex]:
        if neighbor not in visited:
            dfs_recursive(grath, neighbor, visited)
            
# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Виклик функції DFS
dfs_recursive(graph, 'A')

# Ітеративна реалізація алгоритму DFS виглядає таким чином:

def dfs_iterative(graph, start_vertex):
    visited = set()
# Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))  

# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Виклик функції DFS
dfs_iterative(graph, 'A')

'''Алгоритм BFS (ширина) починається з вибраної вершини та відвідує всі її сусідні вершини, 
перш ніж перейти до сусідів цих сусідів.
BFS продовжує відвідувати вершини в ширину графа, перш ніж переходить глибше'''

# Ітеративна реалізація алгоритму BFS виглядає таким чином:
from collections import deque

def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited  

# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Запуск алгоритму BFS
bfs_iterative(graph, 'A')


# Рекурсивна реалізація BFS може бути трохи менш прямолінійною через властивості черги, яка використовується в BFS.

from collections import deque

def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)

# Представлення графа за допомогою списку суміжності
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# Запуск рекурсивного алгоритму BFS
bfs_recursive(graph, deque(["A"]))



# Основи роботи з бібліотекою networkX

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("A")
G.add_nodes_from(["B", "C", "D"])

G.add_edge("A", "B")
G.add_edges_from([("A", "C"), ("B", "C"), ("B", "D")])

num_nodes = G.number_of_nodes()  # 4
num_edges = G.number_of_edges()  # 4
is_connected = nx.is_connected(G)  # True




import networkx as nx
import matplotlib.pyplot as plt

# Створення орієнтованого графа
G = nx.DiGraph()

# Додавання ребер
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 3), (4, 1)])

# Малювання графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)

plt.show()

import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(8)
pos = nx.random_layout(G)
nx.draw(G, pos, with_labels=True)
plt.title("Random Layout")
plt.show()
