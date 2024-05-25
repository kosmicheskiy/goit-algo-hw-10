import numpy as np

# Кількість випадкових точок
n = 100000

# Генеруємо випадкові точки всередині прямокутника [a, b] x [0, max(y)]
x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, max(y), n)

# Обчислюємо, скільки точок потрапило під криву
points_under_curve = sum(y_random <= f(x_random))

# Обчислюємо відношення точок під кривою до загальної кількості точок
area_ratio = points_under_curve / n

# Обчислюємо площу прямокутника та наближену площу під кривою
rectangle_area = (b - a) * max(y)
curve_area = rectangle_area * area_ratio

print("Наближена площа під кривою за допомогою методу Монте-Карло:", curve_area)
