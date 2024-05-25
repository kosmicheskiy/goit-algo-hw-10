from pulp import LpMaximize, LpProblem, LpVariable

# Ініціалізація моделі
model = LpProblem(name="maximize_production", sense=LpMaximize)

# Інгредієнти та обмеження ресурсів
water = LpVariable(name="water", lowBound=0)
sugar = LpVariable(name="sugar", lowBound=0)
lemon_juice = LpVariable(name="lemon_juice", lowBound=0)
fruit_puree = LpVariable(name="fruit_puree", lowBound=0)

# Функція максимізації
model += water + sugar + lemon_juice + fruit_puree

# Обмеження на ресурси
model += 2 * water + fruit_puree <= 100
model += sugar <= 50
model += lemon_juice <= 30
model += 2 * water + fruit_puree <= 40

# Виробництво одиниці "Лимонаду" та "Фруктового соку"
model += 2 * water >= 2
model += sugar >= 1
model += lemon_juice >= 1
model += fruit_puree >= 2

# Вирішення моделі
model.solve()

# Виведення результатів
print("Optimal Production:")
print("Lemonade:", lemon_juice.value())
print("Fruit Juice:", fruit_puree.value())
