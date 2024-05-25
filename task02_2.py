from scipy.integrate import quad

# Обчислення точного значення інтегралу
exact_integral, _ = quad(f, a, b)

print("Точне значення інтегралу:", exact_integral)
#Точне значення інтегралу: 2.666666666666667
