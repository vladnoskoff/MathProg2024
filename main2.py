import matplotlib.pyplot as plt

# Данные о количестве проданных товаров по категориям
categories = ['Категория 1', 'Категория 2', 'Категория 3', 'Категория 4']
sales = [10, 20, 30, 40]

# Создаем круговую диаграмму
plt.figure(figsize=(8, 8))  # Размер фигуры
plt.pie(sales, labels=categories, autopct='%1.1f%%', startangle=90)

# Добавляем заголовок
plt.title('Процентное соотношение продаж по категориям')

# Отображаем диаграмму
plt.axis('equal')  # Чтобы круг выглядел как круг
plt.show()
