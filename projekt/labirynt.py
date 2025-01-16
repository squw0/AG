
#   https://github.com/olapolacik

#  Pamiętaj o zainstalowaniu -  pip install pygame



import pygame
import sys
import heapq

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)

# Load the background image for the menu
MENU_BACKGROUND = pygame.image.load("projekt/mysz.PNG")
MENU_BACKGROUND = pygame.transform.scale(MENU_BACKGROUND, (WIDTH, HEIGHT))

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

def draw_text_with_background(text, font, text_color, bg_color, surface, x, y):
    textobj = font.render(text, True, text_color, bg_color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    pygame.draw.rect(surface, bg_color, textrect)
    pygame.draw.rect(surface, BLACK, textrect, 2)  # Add border
    surface.blit(textobj, textrect)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Grid initialization
def create_grid():
    return [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_grid(grid, path=[], start=None, end=None):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = WHITE if grid[y][x] == 0 else BLACK
            if (x, y) in path:
                color = GREEN
            if start == (x, y):
                color = BLUE
            if end == (x, y):
                color = YELLOW
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}

    g_score = {(x, y): float('inf') for x in range(GRID_SIZE) for y in range(GRID_SIZE)}
    f_score = {(x, y): float('inf') for x in range(GRID_SIZE) for y in range(GRID_SIZE)}

    g_score[start] = 0
    f_score[start] = heuristic(start, end)

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < GRID_SIZE and 0 <= neighbor[1] < GRID_SIZE:
                if grid[neighbor[1]][neighbor[0]] == 1:
                    continue

                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []

def show_controls():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text("Controls", font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
        draw_text("Left Click: Place Wall", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 4 + 50)
        draw_text("Right Click: Remove Wall", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 4 + 100)
        draw_text("S: Set Start Point", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 4 + 150)
        draw_text("E: Set End Point", small_font, BLACK, screen, WIDTH // 2, HEIGHT // 4 + 200)
        draw_text_with_background("Back to Menu", small_font, RED, GRAY, screen, WIDTH // 2, HEIGHT - 100)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH // 2 - 100 < x < WIDTH // 2 + 100 and HEIGHT - 125 < y < HEIGHT - 75:
                    running = False

def main_menu():
    running = True
    while running:
        screen.blit(MENU_BACKGROUND, (0, 0))  # Display the background image
        draw_text("Miłosz to ketaminiarz", font, WHITE, screen, WIDTH // 2, HEIGHT // 4)
        draw_text_with_background("Start Game", small_font, RED, WHITE, screen, WIDTH // 2, HEIGHT // 2 - 50)
        draw_text_with_background("Controls", small_font, RED, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 50)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if WIDTH // 2 - 100 < x < WIDTH // 2 + 100 and HEIGHT // 2 - 75 < y < HEIGHT // 2 - 25:
                    return "game"
                if WIDTH // 2 - 100 < x < WIDTH // 2 + 100 and HEIGHT // 2 + 25 < y < HEIGHT // 2 + 75:
                    return "controls"

def main():
    while True:
        selection = main_menu()
        if selection == "game":
            game_loop()
        elif selection == "controls":
            show_controls()

def game_loop():
    clock = pygame.time.Clock()
    grid = create_grid()
    start = None
    end = None
    path = []
    running = True

    while running:
        screen.fill(WHITE)
        draw_grid(grid, path, start, end)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x //= CELL_SIZE
                y //= CELL_SIZE
                grid[y][x] = 1

            if pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                x //= CELL_SIZE
                y //= CELL_SIZE
                grid[y][x] = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    x, y = pygame.mouse.get_pos()
                    start = (x // CELL_SIZE, y // CELL_SIZE)
                if event.key == pygame.K_e:
                    x, y = pygame.mouse.get_pos()
                    end = (x // CELL_SIZE, y // CELL_SIZE)
                if event.key == pygame.K_SPACE and start and end:
                    path = a_star(grid, start, end)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
