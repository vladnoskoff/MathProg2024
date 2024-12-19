import tkinter as tk


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Лабиринт")
        self.geometry("450x450")

        self.maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        ]

        self.player_x = 0
        self.player_y = 1
        self.cell_size = 40

        self.canvas = tk.Canvas(self, width=450, height=450)
        self.canvas.pack()

        self.path = []  # Список для хранения пути игрока

        self.bind("<Key>", self.on_key_down)
        self.draw_maze()

    def draw_maze(self):
        self.canvas.delete("all")
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                color = "black" if self.maze[y][x] == 1 else "white"
                self.canvas.create_rectangle(
                    x * self.cell_size,
                    y * self.cell_size,
                    (x + 1) * self.cell_size,
                    (y + 1) * self.cell_size,
                    fill=color
                )
                if x == self.player_x and y == self.player_y:
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="blue"
                    )
                if x == 8 and y == 9:  # Выход
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="green"
                    )


# Управление
    def on_key_down(self, event):
        new_x = self.player_x
        new_y = self.player_y

        if event.keysym == "Up":
            new_y -= 1
        elif event.keysym == "Down":
            new_y += 1
        elif event.keysym == "Left":
            new_x -= 1
        elif event.keysym == "Right":
            new_x += 1

        if (0 <= new_x < len(self.maze[0]) and 0 <= new_y < len(self.maze) and self.maze[new_y][new_x] == 0):

            # Добавляем текущую позицию в путь для отрисовки в конце игры
            self.path.append((self.player_x, self.player_y))

            # Обновляем позицию игрока
            self.player_x = new_x
            self.player_y = new_y

            # Проверка на выход
            if (self.player_x == 8 and self.player_y == 9):
                self.end_game()
                return

            # Рисуем путь
            self.draw_path()

        # Обновляем отрисовку лабиринта и игрока
        self.draw_maze()


# Функция для отрисовки проделанного пути
    def draw_path(self):
        for (px, py) in self.path:
            self.canvas.create_rectangle(
                px * self.cell_size,
                py * self.cell_size,
                (px + 1) * self.cell_size,
                (py + 1) * self.cell_size,
                fill="red"
            )

    def end_game(self):
        # Отображаем путь после достижения выхода
        self.draw_path()
        # Отключаем обработку событий клавиатуры
        self.unbind("<Key>")


if __name__ == "__main__":
    game = Game()
    game.mainloop()