import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Крестики нолики")

        self.SIZE = 300
        self.CELL = self.SIZE // 3

        self.canvas = tk.Canvas(self.root, width=self.SIZE, height=self.SIZE, bg="white")
        self.canvas.pack()

        self.board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(None)
            self.board.append(row)

        self.current_player = "X"      # человек начинает
        self.game_active = True
        self.difficulty = "smart"      # по умолчанию умный бот

        # Кнопки
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        btn_easy = tk.Button(frame, text="Легкий", command=self.set_easy, width=12)
        btn_easy.pack(side="left", padx=5)

        btn_smart = tk.Button(frame, text="Умный", command=self.set_smart, width=12)
        btn_smart.pack(side="left", padx=5)

        btn_restart = tk.Button(frame, text="Новая игра", command=self.restart, width=12)
        btn_restart.pack(side="left", padx=5)

        # Привязка мыши
        self.canvas.bind("<Button-1>", self.click)

        # Первая отрисовка
        self.draw_board()

    # Графика
    def draw_board(self):
        self.canvas.delete("all")

        # Сетка
        for i in range(1, 3):
            x = i * self.CELL
            self.canvas.create_line(x, 0, x, self.SIZE, fill="black", width=2)
        for i in range(1, 3):
            y = i * self.CELL
            self.canvas.create_line(0, y, self.SIZE, y, fill="black", width=2)

        # Крестики и нолики
        for row in range(3):
            for col in range(3):
                symbol = self.board[row][col]
                if symbol is not None:
                    x_center = col * self.CELL + self.CELL // 2
                    y_center = row * self.CELL + self.CELL // 2
                    if symbol == "X":
                        color = "blue"
                    else:
                        color = "red"
                    self.canvas.create_text(
                        x_center, y_center, text=symbol,
                        font=("Arial", 48, "bold"), fill=color
                    )

        # Метка сложности
        if self.difficulty == "smart":
            mode_text = "Умный"
        else:
            mode_text = "Лёгкий"
        self.canvas.create_text(
            10, 10, anchor="nw", text=mode_text,
            font=("Arial", 12), fill="gray"
        )

    # Проверка победителя
    def check_winner(self, state=None):
        if state is None:
            state = self.board

        # Строки
        for i in range(3):
            if state[i][0] == state[i][1] == state[i][2] and state[i][0] is not None:
                return state[i][0]

        #Столбцы
        for i in range(3):
            if state[0][i] == state[1][i] == state[2][i] and state[0][i] is not None:
                return state[0][i]

        #Диагонали
        if state[0][0] == state[1][1] == state[2][2] and state[0][0] is not None:
            return state[0][0]
        if state[0][2] == state[1][1] == state[2][0] and state[0][2] is not None:
            return state[0][2]

        #Ничья
        all_filled = True
        for i in range(3):
            for j in range(3):
                if state[i][j] is None:
                    all_filled = False
                    break
            if not all_filled:
                break
        if all_filled:
            return "Draw"

        return None

    #Умный бот
    def minimax(self, state, depth, is_max):
        winner = self.check_winner(state)
        if winner == "O":
            return (10 - depth, None)
        elif winner == "X":
            return (depth - 10, None)
        elif winner == "Draw":
            return (0, None)

        if is_max:  # ход компьютера
            best = -float("inf")
            best_move = None
            for i in range(3):
                for j in range(3):
                    if state[i][j] is None:
                        state[i][j] = "O"
                        score = self.minimax(state, depth + 1, False)[0]
                        state[i][j] = None
                        if score > best:
                            best = score
                            best_move = (i, j)
            return (best, best_move)
        else:       # ход игрока (X)
            best = float("inf")
            best_move = None
            for i in range(3):
                for j in range(3):
                    if state[i][j] is None:
                        state[i][j] = "X"
                        score = self.minimax(state, depth + 1, True)[0]
                        state[i][j] = None
                        if score < best:
                            best = score
                            best_move = (i, j)
            return (best, best_move)

    def get_smart_move(self, state):
        _, move = self.minimax(state, 0, True)
        return move


    #Лёгкий бот
    def get_random_move(self, state):
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if state[r][c] is None:
                    empty_cells.append((r, c))
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return None

    # Игровой процесс
    def player_move(self, row, col):
        if not self.game_active or self.current_player != "X" or self.board[row][col] is not None:
            return

        self.board[row][col] = "X"
        self.draw_board()

        result = self.check_winner()
        if result:
            self.end_game(result)
        else:
            self.current_player = "O"
            self.root.after(300, self.computer_move)

    def computer_move(self):
        if not self.game_active or self.current_player != "O":
            return

        if self.difficulty == "smart":
            move = self.get_smart_move(self.board)
        else:
            move = self.get_random_move(self.board)

        if move:
            row, col = move
            self.board[row][col] = "O"
            self.draw_board()

            result = self.check_winner()
            if result:
                self.end_game(result)
            else:
                self.current_player = "X"

    def end_game(self, result):
        self.game_active = False
        if result == "Draw":
            msg = "Ничья!"
        else:
            msg = f"Победил {result}!"
        messagebox.showinfo("Итог", msg)

    def restart(self):
        #Очистка поля
        self.board = []
        for _ in range(3):
            row = []
            for _ in range(3):
                row.append(None)
            self.board.append(row)

        self.game_active = True
        self.current_player = "X"
        self.draw_board()

    def set_easy(self):
        self.difficulty = "easy"
        self.restart()

    def set_smart(self):
        self.difficulty = "smart"
        self.restart()


    def click(self, event):
        if not self.game_active:
            return
        col = event.x // self.CELL
        row = event.y // self.CELL
        self.player_move(row, col)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()