import pygame
import csv
import sys


pygame.init()


screen_width = 800
screen_height = 600


WHITE = (255, 255, 255)
BLACK = (1, 1, 1)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Фильмы")


font_small = pygame.font.Font(None, 36)
font_large = pygame.font.Font(None, 48)


with open('/home/uer110-08/Desktop/fdfd/movies.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    all_films = list(reader)


genre = ""
films = []
input_text = ""
scroll_position = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if genre == "":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    genre = input_text
                    films = [film[1] for film in all_films if genre.lower() in film[2].lower()]
                    scroll_position = 0
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                scroll_position += 1
            elif event.key == pygame.K_UP:
                scroll_position = max(0, scroll_position - 1)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                genre = ""

    screen.fill(WHITE)

    if genre == "":
        title_text = font_large.render("Напишите жанра фильма в этом окне", True, BLACK)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))
        input_text_render = font_large.render(input_text, True, BLACK)
        screen.blit(input_text_render, (screen_width // 2 - input_text_render.get_width() // 2, 200))
    else:
        title_text = font_large.render(f"Фильмы в жанре  {genre.title()} ", True, BLACK)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 100))

        if len(films) > 0:
            films_per_page = 5
            start_index = scroll_position * films_per_page
            end_index = min(start_index + films_per_page, len(films))

            for i in range(start_index, end_index):
                film = films[i]
                film_text = font_small.render(film, True, BLACK)
                screen.blit(film_text, (screen_width // 2 - film_text.get_width() // 2, 200 + 50 * (i - start_index)))
        else:
            no_films_text = font_small.render("Нет фильмов в этом жанре", True, BLACK)
            screen.blit(no_films_text, (screen_width // 2 - no_films_text.get_width() // 2, 200))

    pygame.display.flip()
