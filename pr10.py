import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Character:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.laps_completed = 0

    def move(self):
        speed = random.randint(1, 5)  # скорость от 1 до 5
        self.position += speed

    def check_lap(self, lap_length):
        if self.position >= lap_length:
            self.laps_completed += 1
            self.position = 0


def race(characters, laps_to_complete, lap_length):
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')
    ax.set_title("Гонка персонажей")

    # Создаем круг для гонки
    circle = plt.Circle((0, 0), 0.9, color='lightgray', fill=False)
    ax.add_artist(circle)

    # Создаем линии для каждого персонажа
    lines = [ax.plot([], [], marker='o', label=char.name)[0] for char in characters]

    # Создаем текстовые аннотации для отображения количества кругов
    texts = [ax.text(1.05, 0.9 - i * 0.1, f"{char.name}: 0", fontsize=10) for i, char in enumerate(characters)]

    def init():
        for line in lines:
            line.set_data([], [])
        return lines + texts

    def update(frame):
        for char in characters:
            char.move()
            char.check_lap(lap_length)

            # Обновляем позицию на круге
            angle = (char.position / lap_length) * 2 * np.pi  # Преобразуем позицию в угол
            x = 0.9 * np.cos(angle)
            y = 0.9 * np.sin(angle)

            # Обновляем линию для персонажа
            lines[characters.index(char)].set_data(x, y)

            # Обновляем текстовое отображение количества кругов рядом с именем персонажа
            texts[characters.index(char)].set_text(f"{char.name}: {char.laps_completed}")

            # Устанавливаем позицию текста рядом с персонажем
            text_x = 1.05
            text_y = 0.9 - characters.index(char) * 0.1

            # Обновляем позицию текста
            texts[characters.index(char)].set_position((text_x, text_y))

        c = sum(1 for char in characters if char.laps_completed == laps_to_complete)
        if c == len(characters):
            return

        return lines + texts

    ani = animation.FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True)
    plt.legend()
    plt.show()


def main():
    characters_options = ["Таракан", "Собака", "Дед Мороз", "Человечек", "Мультяшный персонаж"]
    print("Выберите участников гонки (введите номера через запятую):")
    for i, character in enumerate(characters_options):
        print(f"{i + 1}. {character}")

    selected_indices = input("Ваш выбор: ")
    selected_indices = [int(i) - 1 for i in selected_indices.split(",") if i.isdigit()]

    if len(selected_indices) < 3 or len(selected_indices) > 5:
        print("Выберите от 3 до 5 участников.")
        return

    characters = [Character(characters_options[i]) for i in selected_indices]
    laps_to_complete = int(input("Введите количество кругов для завершения: "))
    lap_length = 100  # Длина круга (можно изменить)

    race(characters, laps_to_complete, lap_length)


if __name__ == "__main__":
    main()
