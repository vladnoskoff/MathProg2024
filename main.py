import numpy as np
import matplotlib.pyplot as plt

# Задаем размеры изображения
width, height = 500, 500

# Создаем массив для хранения значений пикселей
image = np.zeros((height, width))

# Определяем границы области отображения
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5

# Генерируем фрактал Мандельброта
for x in range(width):
    for y in range(height):
        zx, zy = x * (x_max - x_min) / (width - 1) + x_min, y * (y_max - y_min) / (height - 1) + y_min
        c = complex(zx, zy)
        z = 0
        iteration = 0
        max_iteration = 100

        while abs(z) <= 2 and iteration < max_iteration:
            z = z * z + c
            iteration += 1

        # Сохраняем количество итераций в массиве
        image[y, x] = iteration

# Визуализируем фрактал
plt.imshow(image, extent=(x_min, x_max, y_min, y_max), cmap='hot')
plt.colorbar()
plt.title("Фрактал Мандельброта")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
