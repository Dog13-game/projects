


import pygame

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Рух об'єкта за допомогою стрілок")

screen.fill((255, 255, 255))  # Заповнюємо фон білим кольором

# Позиція об'єкта
rect_position = pygame.math.Vector2(100, 100)  # Початкова позиція (Vector2)
object_size = 100  # Розмір об'єкта
object_color = (255, 0, 0)  # Колір об'єкта (червоний)

# Основний цикл програми
running = True
while running:
    screen.fill((255, 255, 255))  # Заповнюємо фон білим кольором

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Якщо користувач закрив вікно
            running = False
        elif event.type == pygame.KEYDOWN:  # Якщо натиснута клавіша
            if event.key == pygame.K_RIGHT:  # Стрілка вправо
                rect_position.x += 50
            elif event.key == pygame.K_LEFT:  # Стрілка вліво
                rect_position.x -= 50

    # Малюємо об'єкт (квадрат)
    pygame.draw.rect(screen, object_color, (rect_position.x, rect_position.y, object_size, object_size))

    # Оновлення екрану
    pygame.display.flip()

# Закриття Pygame
pygame.quit()

