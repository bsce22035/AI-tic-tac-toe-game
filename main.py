import tkinter as tk
import math
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg="#1e1e2f")
        self.board = [' ' for _ in range(9)]
        self.buttons = []
        self.player_starts = True
        self.difficulty = tk.StringVar(value="Hard")
        self.score = {"Player": 0, "Computer": 0, "Draws": 0}
        self.highlighted = []
        self.setup_ui()

    def setup_ui(self):
        # Styling frame
        header = tk.Frame(self.root, bg="#1e1e2f")
        header.grid(row=0, column=0, columnspan=3, pady=10)

        tk.Label(header, text="Difficulty:", fg="white", bg="#1e1e2f", font=('Arial', 12)).pack(side=tk.LEFT)
        tk.OptionMenu(header, self.difficulty, "Easy", "Medium", "Hard").pack(side=tk.LEFT, padx=5)

        tk.Button(header, text="Player Starts", bg="#4caf50", fg="white", font=('Arial', 10), command=self.set_player_first).pack(side=tk.LEFT, padx=5)
        tk.Button(header, text="Computer Starts", bg="#f44336", fg="white", font=('Arial', 10), command=self.set_computer_first).pack(side=tk.LEFT, padx=5)

        # Game board
        for i in range(9):
            btn = tk.Button(self.root, text=' ', font='Helvetica 26 bold', width=5, height=2,
                            bg="#282c34", fg="white", activebackground="#3e4451",
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=1 + i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        # Result and Score
        self.result_label = tk.Label(self.root, text="", font='Helvetica 14 bold', fg="cyan", bg="#1e1e2f")
        self.result_label.grid(row=4, column=0, columnspan=3, pady=5)

        self.score_label = tk.Label(self.root, text=self.get_score_text(), font='Helvetica 12', fg="white", bg="#1e1e2f")
        self.score_label.grid(row=5, column=0, columnspan=3, pady=5)

        # Controls
        tk.Button(self.root, text="Play Again", font=('Arial', 11), bg="#2196f3", fg="white", command=self.reset_game).grid(row=6, column=0, columnspan=2, sticky="ew", padx=2, pady=10)
        tk.Button(self.root, text="Reset Scores", font=('Arial', 11), bg="#9c27b0", fg="white", command=self.reset_scores).grid(row=6, column=2, sticky="ew", padx=2, pady=10)

        if not self.player_starts:
            self.root.after(500, self.computer_move)

    def set_player_first(self):
        self.player_starts = True
        self.reset_game()

    def set_computer_first(self):
        self.player_starts = False
        self.reset_game()

    def get_score_text(self):
        return f"Player: {self.score['Player']} | Computer: {self.score['Computer']} | Draws: {self.score['Draws']}"

    def player_move(self, i):
        if self.board[i] == ' ':
            self.animate_button(i, 'X')
            self.board[i] = 'X'
            if not self.check_game_over():
                self.root.after(400, self.computer_move)

    def computer_move(self):
        move = self.get_computer_move()
        if move is not None:
            self.animate_button(move, 'O')
            self.board[move] = 'O'
        self.check_game_over()

    def animate_button(self, i, symbol):
        btn = self.buttons[i]
        btn.config(text=symbol, state='disabled', disabledforeground="#ffeb3b" if symbol == 'X' else "#00bcd4")
        btn.update()

    def get_computer_move(self):
        empty = [i for i, spot in enumerate(self.board) if spot == ' ']
        level = self.difficulty.get()
        if level == "Easy":
            return random.choice(empty)
        elif level == "Medium" and random.random() < 0.5:
            return random.choice(empty)
        return self.find_best_move()

    def find_best_move(self):
        best_score = -math.inf
        move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def minimax(self, is_maximizing):
        if self.is_winner('O'):
            return 1
        if self.is_winner('X'):
            return -1
        if ' ' not in self.board:
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score = self.minimax(False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score = self.minimax(True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def is_winner(self, player):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in wins:
            if all(self.board[i] == player for i in combo):
                self.highlighted = combo
                return True
        return False

    def check_game_over(self):
        if self.is_winner('X'):
            self.score['Player'] += 1
            self.end_game("You win!", "X")
            return True
        elif self.is_winner('O'):
            self.score['Computer'] += 1
            self.end_game("Computer wins!", "O")
            return True
        elif ' ' not in self.board:
            self.score['Draws'] += 1
            self.end_game("It's a draw!", None)
            return True
        return False

    def end_game(self, message, winner):
        self.result_label.config(text=message)
        self.score_label.config(text=self.get_score_text())
        for btn in self.buttons:
            btn.config(state='disabled')

        if winner:
            for i in self.highlighted:
                self.buttons[i].config(bg="#ff9800")
        self.highlighted.clear()

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for btn in self.buttons:
            btn.config(text=' ', state='normal', bg="#282c34")
        self.result_label.config(text="")
        if not self.player_starts:
            self.root.after(500, self.computer_move)

    def reset_scores(self):
        self.score = {"Player": 0, "Computer": 0, "Draws": 0}
        self.score_label.config(text=self.get_score_text())
        self.reset_game()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
