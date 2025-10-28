import numpy as np

# Pedir condiciones iniciales

height = -1

while not height >= 0:
    height = float(input("\nPlease enter the initial height (m): "))

velocity_y = float(input("\nPlease enter the initial vertical velocity (m/s): "))
g = 9.81

# Calcular el tiempo total hasta que la altura sea 0
t_total = (velocity_y + np.sqrt(velocity_y**2 + 2 * g * height)) / g

# Crear un array de tiempos (de 0 a t_total, paso de 0.5 s)
t = np.arange(0, t_total + 0.5, 0.5)

# Calcular la altura para cada instante
y = height + velocity_y * t - 0.5 * g * t**2

# Asegurar que la altura no sea negativa
y = np.maximum(y, 0)

# Calcular las diferencias entre alturas consecutivas
dy = np.diff(y)

# Calcular la media de esas diferencias
mean_dy = np.mean(dy)

# Mostrar resultados
print("\nAlturas en función del tiempo:")
for ti, yi in zip(t, y):
    print(f"t = {ti:.1f} s → altura = {yi:.2f} m")
    if yi <= 0:
        break

print("\nDiferencias entre alturas consecutivas:")
print(dy)

print(f"\nMedia de las diferencias: {mean_dy:.4f} m por paso")