import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Змінні рішення
lemon_juice = pulp.LpVariable('LemonJuice', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Цільова функція
model += lemon_juice + fruit_juice, "Maximize_Juice_Production"

# Обмеження
model += 2*lemon_juice + fruit_juice <= 100, "Water_Juice_Constraint"
model += lemon_juice <= 50, "Sugar_Juice_Constraint"
model += lemon_juice <= 30, "Lemon_Juice_Constraint"
model += 2*fruit_juice <= 40, "FruitPuree_Juice_Constraint"

# Розв'язання проблеми
model.solve()

# Виведення результатів
print("Optimal Production:")
print("Lemon Juice:", lemon_juice.value())
print("Fruit Juice:", fruit_juice.value())
print("Total Juice Production:", lemon_juice.value() + fruit_juice.value())

#Optimal Production:
#Lemon Juice: 30.0
#Fruit Juice: 20.0
#Total Juice Production: 50.0
