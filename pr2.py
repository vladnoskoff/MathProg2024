import pygame
from pygame.locals import *

# Константы
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (7, 7), 7)
        self.rect = self.image.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
        self.dx = 5
        self.dy = -5

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT - 30))


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((75, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Arkanoid")
        self.clock = pygame.time.Clock()

        # Создание спрайтов
        self.balls = pygame.sprite.Group(Ball(), Ball())  # Создаем два шара
        self.paddle = Paddle()
        self.bricks = pygame.sprite.Group()

        for x in range(0, DISPLAY_WIDTH, 80):
            for y in range(50, 150, 30):
                brick = Brick(x, y)
                self.bricks.add(brick)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.balls.draw(self.screen)  # Рисуем оба шара
        self.screen.blit(self.paddle.image, self.paddle.rect)
        self.bricks.draw(self.screen)
        pygame.display.flip()

    def update(self):
        self.balls.update()  # Обновляем оба шара

        for ball in self.balls:
            # Обработка столкновения мяча с ракеткой
            if ball.rect.colliderect(self.paddle.rect):
                ball.dy = -ball.dy

            # Обработка столкновения мяча с кирпичами
            brick_hit_list = pygame.sprite.spritecollide(ball, self.bricks, True)
            for brick in brick_hit_list:
                ball.dy = -ball.dy

            # Проверка на столкновение с границами экрана
            if ball.rect.left <= 0 or ball.rect.right >= DISPLAY_WIDTH:
                ball.dx = -ball.dx
            if ball.rect.top <= 0:
                ball.dy = -ball.dy
            if ball.rect.bottom >= DISPLAY_HEIGHT:
                print("Game Over")
                pygame.quit()

            # Проверка на столкновение между шарами
            for other_ball in self.balls:
                if other_ball != ball and ball.rect.colliderect(other_ball.rect):
                    # Отскок шаров друг от друга
                    ball.dx, other_ball.dx = other_ball.dx, ball.dx
                    ball.dy, other_ball.dy = other_ball.dy, ball.dy

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[K_LEFT] and self.paddle.rect.left > 0:
                self.paddle.rect.x -= 5
            if keys[K_RIGHT] and self.paddle.rect.right < DISPLAY_WIDTH:
                self.paddle.rect.x += 5

            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
