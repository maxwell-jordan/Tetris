from random import randrange
import keyboard as kb
import os


def main():
    xPos = -1
    yPos = -1
    grid = [["-" for i in range(10)] for i in range(10)]
    print_grid(grid)
    newBlock = True
    curr = 1
    frameCount = 0

    while True:  # making a loop
        if frameCount == 0:
            clear_grid(grid)
            newBlock = True
        if newBlock:
            curr = choose_new_tetrimino()
            newBlock = False
        if curr == 1: #square
            grid[0][5] = "#"
            grid[0][4] = "#"
            grid[1][5] = "#"
            grid[1][4] = "#"
        elif curr == 2: #line piece
            grid[0][5] = "#"
            grid[1][5] = "#"
            grid[2][5] = "#"
            grid[3][5] = "#"
        elif curr == 3: #L block
            grid[0][5] = "#"
            grid[1][5] = "#"
            grid[2][5] = "#"
            grid[2][6] = "#"
        elif curr == 4: #reverse L block
            grid[0][5] = "#"
            grid[1][5] = "#"
            grid[2][5] = "#"
            grid[2][4] = "#"
        elif curr == 5: #T Block
            grid[0][5] = "#"
            grid[0][6] = "#"
            grid[0][4] = "#"
            grid[1][5] = "#"
        elif curr == 6: #S block
            grid[0][4] = "#"
            grid[0][5] = "#"
            grid[1][5] = "#"
            grid[1][6] = "#"
        elif curr == 7: #Z block
            grid[0][5] = "#"
            grid[0][6] = "#"
            grid[1][5] = "#"
            grid[1][4] = "#"


        print_grid(grid)
        os.system('clear')
        if kb.is_pressed(' '):  # if key 'q' is pressed
            print('Goodbye.')
            break  # finishing the loop
        frameCount+=1
        if frameCount == 200:
            frameCount = 0
    return


def print_grid(grid):
    for row in grid:
        print("\t", end="")
        for a in row:
            print(a, end="")
        print("\n")

def clear_grid(grid):
    for row in range(10):
        for a in range(10):
            grid[row][a] = '-'

def choose_new_tetrimino():
    a = randrange(7)
    return a + 1


if __name__ == "__main__":
    main()

