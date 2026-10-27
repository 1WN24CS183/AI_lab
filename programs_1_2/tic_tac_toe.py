import math

class TicTacToe:
    def __init__(self):
        # Initialize an empty 3x3 board
        self.board = [['_' for _ in range(3)] for _ in range(3)]
        self.human = 'X'
        self.computer = 'O'

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def is_moves_left(self):
        for row in self.board:
            if '_' in row:
                return True
        return False

    def evaluate(self):
        # Check rows for win condition
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '_':
                return 1 if self.board[row][0] == self.computer else -1

        # Check columns for win condition
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '_':
                return 1 if self.board[0][col] == self.computer else -1

        # Check main diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '_':
            return 1 if self.board[0][0] == self.computer else -1

        # Check anti-diagonal
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '_':
            return 1 if self.board[0][2] == self.computer else -1

        return 0

    def minimax(self, depth, is_max):
        score = self.evaluate()

        # Terminal states
        if score == 1 or score == -1:
            return score
        if not self.is_moves_left():
            return 0

        if is_max:
            best = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_':
                        self.board[i][j] = self.computer
                        best = max(best, self.minimax(depth + 1, False))
                        self.board[i][j] = '_'
            return best
        else:
            best = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == '_':
                        self.board[i][j] = self.human
                        best = min(best, self.minimax(depth + 1, True))
                        self.board[i][j] = '_'
            return best

    def find_best_move(self):
        best_val = -math.inf
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    self.board[i][j] = self.computer
                    move_val = self.minimax(0, False)
                    self.board[i][j] = '_'

                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val

        return best_move

    def play(self):
        print("Initial Board:")
        self.print_board()

        while True:
            # Human turn
            while True:
                try:
                    move = input("Enter row and column (e.g., '1 1'): ").split()
                    r, c = int(move[0]) - 1, int(move[1]) - 1
                    if 0 <= r < 3 and 0 <= c < 3 and self.board[r][c] == '_':
                        self.board[r][c] = self.human
                        break
                    else:
                        print("Position occupied or out of bounds. Try again.")
                except (ValueError, IndexError):
                    print("Invalid input format. Enter two numbers between 1 and 3.")

            self.print_board()

            if self.evaluate() == -1:
                print("Human Player Wins")
                break
            if not self.is_moves_left():
                print("Game Draw")
                break

            # Computer turn
            print("Computer's Move:")
            comp_move = self.find_best_move()
            if comp_move != (-1, -1):
                self.board[comp_move[0]][comp_move[1]] = self.computer

            self.print_board()

            if self.evaluate() == 1:
                print("Computer Wins")
                break
            if not self.is_moves_left():
                print("Game Draw")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play()