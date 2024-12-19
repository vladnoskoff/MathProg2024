def print_maze(maze):
    for row in maze:
        print(' '.join(['#' if cell == 1 else ' ' for cell in row]))


def dfs(maze, start, end):
    stack = [start]
    visited = set()
    path = {}

    while stack:
        current = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            break

        x, y = current
        neighbors = [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

        for neighbor in neighbors:
            nx, ny = neighbor
            if (0 <= nx < len(maze)) and (0 <= ny < len(maze[0])) and (maze[nx][ny] == 0) and (neighbor not in visited):
                stack.append(neighbor)
                path[neighbor] = current

    # Восстанавливаем путь
    real_path = []
    step = end

    while step in path:
        real_path.append(step)
        step = path[step]

    real_path.append(start)
    real_path.reverse()

    return real_path


def compare_paths(real_path, model_path):
    return real_path == model_path


def main():
    maze = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    ]

    print_maze(maze)

    start = (1, 1)
    end = (9, 8)

    real_path = [
        (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4),
        (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2),
        (5, 1), (6, 1), (7, 1), (7, 2), (7, 3), (7, 4),
        (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (9, 8)
    ]

    model_path = dfs(maze, start, end)

    print("Найденный путь:")
    print(model_path)

    # Сравнение путей
    if compare_paths(real_path, model_path):
        print("Найденный путь совпадает с модельным.")
    else:
        print("Найденный путь не совпадает с модельным.")


if __name__ == "__main__":
    main()
