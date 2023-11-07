import tkinter as tk
from tkinter import messagebox

WINNING_COMBINATIONS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

def evaluate(board):
    for combination in WINNING_COMBINATIONS:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != "":
            return board[combination[0]]
        
    if "" not in board:
        return "Empate"
    return None

def minimax(board, depth, is_maximizing):
    result = evaluate(board)
    if result is not None:
        if result == "X":
            return -1
        elif result == "O":
            return 1
        else:
            return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board[:], depth + 1, False)
                best_score = max(score, best_score)
                board[i] = ""
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board[:], depth + 1, True)
                best_score = min(score, best_score)
                board[i] = ""
        return best_score

def player_click(index):
    global board
    if board[index] == "":
        buttons[index].config(text="X", state=tk.DISABLED)
        board[index] = "X"
        if evaluate(board) == "X":
            messagebox.showinfo("Tic Tac Toe", "You win!.")
            root.destroy()
        elif evaluate(board) is None:
            ai_move()
        else:
            messagebox.showinfo("Tic Tac Toe", "Draw.")
            root.destroy()

def ai_move():
    global board
    best_score = float("-inf")
    best_move = -1
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board[:], 0, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    if best_move != -1:
        board[best_move] = "O"
        buttons[best_move].config(text="O", state=tk.DISABLED)
        if evaluate(board) == "O":
            messagebox.showinfo("Tic Tac Toe", "You loose!.")
            root.destroy()

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300  
window_height = 300 
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.title("Tic Tac Toe")
root.resizable(False, False)
tk_frame = tk.Frame(root)
tk_frame.pack()

board = [""] * 9
buttons = []

for i in range(9):
    button = tk.Button(tk_frame, text=" ", font=("normal", 20), width=5, height=2, command=lambda i=i: player_click(i))
    buttons.append(button)
    row = i // 3
    col = i % 3
    button.grid(row=row, column=col)

root.mainloop()
