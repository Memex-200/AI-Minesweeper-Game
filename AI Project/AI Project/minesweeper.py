import random


class MinesweeperSolver:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[" " for _ in range(cols)] for _ in range(rows)]
        self.visited = [[False for _ in range(cols)] for _ in range(rows)]
        self.generate_mines()

    def generate_mines(self):
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in mine_positions:
            row = pos // self.cols
            col = pos % self.cols
            self.board[row][col] = "M"

    def is_valid(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols

    def count_adjacent_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if self.is_valid(nx, ny) and self.board[nx][ny] == "M":
                    count += 1
        return count

    def dfs(self, x, y):
        if not self.is_valid(x, y) or self.visited[x][y]:
            return

        self.visited[x][y] = True
        mine_count = self.count_adjacent_mines(x, y)

        if mine_count > 0:
            # Flag cells with mines nearby
            print(f"Flag cell at ({x}, {y}) with {mine_count} mines nearby")
        else:
            # No mines nearby, reveal the cell
            print(f"Reveal cell at ({x}, {y}) with 0 mines nearby")

            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.dfs(x + i, y + j)

    def solve(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if not self.visited[i][j]:
                    self.dfs(i, j)


# Example usage:
rows, cols, mines = 10, 5, 1  # Replace with your desired dimensions and number of mines
solver = MinesweeperSolver(rows, cols, mines)
solver.solve()
