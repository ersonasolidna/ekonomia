# Ekonomia 2025-03 Zadanie 1

import numpy as np
import matplotlib.pyplot as plt

# ------------- Parametry użytkowe i budżetowe -------------
# Funkcja użyteczności U(x,y) = (x-3)^0.75 * (y-4)^0.25
def U(x, y):
    return (x - 3) ** 0.75 * (y - 4) ** 0.25

# Budżet: 8x + 2y = 10 000  →  y = (10 000 − 8x)/2
def y_budget(x):
    return (10_000 - 8 * x) / 2

# ------------- Siatka do poziomic --------------------------
x = np.linspace(3.01, 1_400, 400)
y = np.linspace(4.01, 5000, 400)
X, Y = np.meshgrid(x, y)
Z = U(X, Y)

# ------------- Rysunek -------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# Poziomice użyteczności
levels = [900, 1004.18, 1100]
contours = ax.contour(X, Y, Z, levels=levels)
ax.clabel(contours, inline=True, fontsize=8)

# Punkt optymalny
x_star, y_star = 937.5, 1250
ax.scatter([x_star], [y_star], s=60)
ax.annotate(f"({x_star}, {y_star})", (x_star, y_star), textcoords="offset points", xytext=(6, 6))

# Budżet – tylko tam, gdzie y > 4 (żeby pozostać w domenie użyteczności)
x_line = np.linspace(3.01, 1250, 400)  # przy x ≈ 1 249, y_budget ≈ 4
ax.plot(x_line, y_budget(x_line), linewidth=2)

# Opisy osi i tytuł
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Poziomice U(x,y) 900, 1004.18 oraz 1100 wraz z linią budżetową 8x + 2y = 10 000')

plt.show()
