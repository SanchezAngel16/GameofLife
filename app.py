import pygame
import random

#GLOBAL VARS
s_width = 600
s_height = 600
rows = cols = 60
cell_size = s_width / rows

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (255,0,0)

win = pygame.display.set_mode((s_width, s_height))

def make_grid_array(rows, cols):
    return [[0] * cols for i in range(rows)]

def set_initial_board(board):
    for i in range(rows):
        for j in range(cols):
            if random.randrange(0,100) < 60:
                n = 1
            else:
                n = 0
            board[i][j] = n

def draw_board(win, board):
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                pygame.draw.rect(win, WHITE, (j*cell_size, i*cell_size, cell_size, cell_size))

def get_next_generation(old):
    new = make_grid_array(rows,cols)
    for i in range(rows):
        for j in range(cols):
            living_cells = 0
            if i == 0:
                if j == 0:
                    living_cells += old[i][j+1] + old[i+1][j] + old[i+1][j+1]
                elif j == (cols-1):
                    living_cells += old[i][j-1] + old[i-1][j-1] + old[i+1][j]
                else:
                    living_cells += old[i][j-1] + old[i+1][j-1] + old[i+1][j] + old[i+1][j+1] + old[i][j+1]
            elif i == (rows-1):
                if j == 0:
                    living_cells += old[i-1][j] + old[i-1][j+1] + old[i][j+1]
                elif j == (cols-1):
                    living_cells += old[i][j-1] + old[i-1][j-1] + old[i-1][j]
                else:
                    living_cells += old[i][j-1] + old[i-1][j-1] + old[i-1][j] + old[i-1][j+1] + old[i][j+1]
            else:
                if j == 0:
                    living_cells += old[i-1][j] + old[i+1][j] + old[i][j+1] + old[i-1][j+1] + old[i+1][j+1]
                elif j == (cols-1):
                    living_cells += old[i-1][j] + old[i+1][j] + old[i][j-1] + old[i-1][j-1] + old[i+1][j-1]
                else:
                    living_cells += old[i-1][j] + old[i+1][j] + old[i][j-1] + old[i][j+1] + old[i-1][j-1] + old[i+1][j+1] + old[i-1][j+1] + old[i+1][j-1]
            
            if old[i][j] == 1:
                if living_cells >= 2 and living_cells <= 3:
                    new[i][j] = 1
                else:
                    new[i][j] = 0
            else:
                if living_cells == 3:
                    new[i][j] = 1 
    return new

def main():
    run = True
    flag = False
    clock = pygame.time.Clock()
    board = make_grid_array(rows,cols)
    board_2 = make_grid_array(rows,cols)
    set_initial_board(board)
    set_initial_board(board_2)
    while run:
        clock.tick(60)
        win.fill(BLACK)
        if flag:
            board_2 = get_next_generation(board)
            flag = not(flag)
            draw_board(win,board_2)
        else:
            board = get_next_generation(board_2)
            flag = not(flag)
            draw_board(win,board)
        draw_board(win, board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    set_initial_board(board)
    pygame.display.quit()

main()
