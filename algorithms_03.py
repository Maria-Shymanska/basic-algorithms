def factorial(n):
    if n == 0: # базовий випадок
        return 1
    else:
        return n * factorial(n-1) # рекурсивний випадок

print(factorial(5)) # виведе 120


def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55



def sum_iter(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result

print(sum_iter(5)) # виведе 15



import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_triangle(vertices, ax):
    triangle = patches.Polygon(vertices, fill=False, edgecolor='black')
    ax.add_patch(triangle)

def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

def sierpinski(vertices, level, ax):
    draw_triangle(vertices, ax)
    if level > 0:
        sierpinski([vertices[0], midpoint(vertices[0], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)
        sierpinski([vertices[1], midpoint(vertices[0], vertices[1]), midpoint(vertices[1], vertices[2])], level-1, ax)
        sierpinski([vertices[2], midpoint(vertices[2], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()
    vertices = [[0, 0], [0.5, 0.75], [1, 0]]
    sierpinski(vertices, 3, ax)
    plt.show()

main()


from pathlib import Path

def display_tree(path: Path, indent: str = "") -> None:
    print(indent + str(path.name))

    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, indent + "    ")

if __name__ == "__main__":
    root = Path("picture")
    display_tree(root)
