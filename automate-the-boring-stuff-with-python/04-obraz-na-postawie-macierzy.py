if __name__ == '__main__':
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', '0', '0', '.', '.', '.'],
            ['0', '0', '0', '0', '.', '.'],
            ['0', '0', '0', '0', '0', '.'],
            ['.', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '.'],
            ['0', '0', '0', '0', '.', '.'],
            ['.', '0', '0', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for i in range(6):
        for j in range(9):
            print(grid[j][i], end="")
        print()
