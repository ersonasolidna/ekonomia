import matplotlib.pyplot as plt
import numpy as np

# Dane
M = 3710
Px_old = 7
Px_new = 4.9
Py = 10

# Funkcja użyteczności U(x,y) = x^0.3*y^0.7 - Cobb-Douglas
def U(x, y):
    return (x) ** 0.3 * (y) ** 0.7

# Wykres budżetu końcowego: y = 371 - 0.49x 
x_vals = np.linspace(0, 800, 300)
y_vals = 371 - 0.49 * x_vals

# Wykres budżetu obrocnego: y = 337.6 - 0.49x
x_vals_obr = np.linspace(0, 800, 300)
y_vals_obr = 337.6 - 0.49 * x_vals_obr

# Wykres budżetu początkowego: y = 371 - 0.7x
x_vals_start = np.linspace(0, 800, 300)
y_vals_start = 371 - 0.7 * x_vals_start

# Poziomice użyteczności
X, Y = np.meshgrid(x_vals, y_vals)
Z = U(X, Y)
# ------------- Rysunek -------------------------------------
#fig, ax = plt.subplots(figsize=(8, 6))
levels = [224.15, 227.02, 249.47]

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, label='Budżet końcowy', color='blue')
plt.plot(x_vals_obr, y_vals_obr, label='Budżet obrócony - sztucznie zaniżony do m prim', color='red')
plt.plot(x_vals_start, y_vals_start, label='Budżet początkowy', color='green')
plt.scatter(227.14, 259.70, color='blue', zorder=5, label='Punkt x=227.14, y=259.70 - koszyk końcowy')
plt.scatter(159, 259.70, color='green', zorder=5, label='Punkt x=159; y=259,70 - koszyk początkowy')
plt.scatter(206.7, 236.33, color='red', zorder=5, label='Punkt x=206,7; y=236,33 - koszyk "obrócony"')
plt.annotate('(227.14, 259.70)', xy=(227.14, 259.70), xytext=(290, 250),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.annotate('(159, 259.70)', xy=(159, 259.70), xytext=(50, 200),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.annotate('(206,7, 236,33)', xy=(206.7, 236.33), xytext=(330, 230),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.xlabel('Dobro x (ilość)')
plt.ylabel('Dobro y (ilość)')
plt.title('E.93.Z2 - Efekt substytucyjny i efekt dochodowy Słuckiego')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.xlim(left=0)
contours = plt.contour(X, Y, Z, levels=levels)
plt.clabel(contours, inline=True, fontsize=8)
plt.show()