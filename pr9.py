import tkinter as tk
import random


class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Лабиринт")
        self.geometry("450x450")
        self.maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        ]

        # Определяем ловушки
        self.traps = {
            (1, 4): "danger",  # Опасное препятствие
            (5, 6): "teleport",  # Телепортирующее препятствие
            (3, 3): "freeze"  # Замораживающее препятствие
        }

        self.start_position = (0, 1)
        self.player_x = self.start_position[0]
        self.player_y = self.start_position[1]
        self.cell_size = 40
        self.canvas = tk.Canvas(self, width=450, height=450)
        self.canvas.pack()
        self.path = []
        self.freeze_turns = 0
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
                if x == 1 and y == 4:
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="orange"
                    )
                if x == 3 and y == 3:
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="blue"
                    )
                if x == 5 and y == 6:
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="violet"
                    )
                if x == self.player_x and y == self.player_y:
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="pink"
                    )
                if x == 8 and y == 9:
                    self.canvas.create_rectangle(
                        x * self.cell_size,
                        y * self.cell_size,
                        (x + 1) * self.cell_size,
                        (y + 1) * self.cell_size,
                        fill="green"
                    )

    def on_key_down(self, event):
        if self.freeze_turns > 0:
            self.freeze_turns -= 1
            return

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

            # Проверка на ловушки
            if (new_x, new_y) in self.traps:
                trap_type = self.traps[(new_x, new_y)]
                if trap_type == "danger":
                    # Возвращаем игрока к старту
                    self.player_x = self.start_position[0]
                    self.player_y = self.start_position[1]
                elif trap_type == "teleport":
                    # Телепортация в случайную клетку
                    while True:
                        teleport_x = 1
                        teleport_y = 5
                        if self.maze[teleport_y][teleport_x] == 0:
                            self.player_x = teleport_x
                            self.player_y = teleport_y
                            break
                elif trap_type == "freeze":
                # Замораживаем игрока на несколько ходов
                    self.player_x = 3
                    self.player_y = 3
                    self.freeze_turns = 2

            else:
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

