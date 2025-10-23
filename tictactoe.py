import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # ตัวแปรเก็บสถานะเกม
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        
        # ตั้งค่าสี (สามารถปรับแต่งได้)
        self.colors = {
            "bg": "#f0f0f0",          # สีพื้นหลัง
            "button": "#ffffff",       # สีปุ่ม
            "x": "#FF6B6B",           # สี X
            "o": "#4ECDC4",           # สี O
            "button_hover": "#e0e0e0"  # สีเมื่อเมาส์ชี้
        }
        
        # ตั้งค่าขนาด (สามารถปรับแต่งได้)
        self.settings = {
            "button_size": 100,        # ขนาดปุ่ม
            "font_size": 48,           # ขนาดตัวอักษร
            "padding": 5               # ระยะห่างระหว่างปุ่ม
        }
        
        self.setup_gui()
        self.create_menu()
    
    def setup_gui(self):
        # สร้างเฟรมหลัก
        self.frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.frame.pack(padx=10, pady=10)
        
        # สร้างปุ่มตาราง 3x3
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.frame,
                    text="",
                    font=("Arial", self.settings["font_size"]),
                    width=2,
                    height=1,
                    bg=self.colors["button"],
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=self.settings["padding"], 
                          pady=self.settings["padding"])
                
                # เพิ่ม hover effect
                button.bind("<Enter>", lambda e, btn=button: self.on_hover(btn, True))
                button.bind("<Leave>", lambda e, btn=button: self.on_hover(btn, False))
                
                self.buttons.append(button)
    
    def create_menu(self):
        # สร้างเมนูบาร์
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # เมนูเกม
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.reset_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.root.quit)
    
    def button_click(self, row, col):
        index = row * 3 + col
        
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(
                text=self.current_player,
                fg=self.colors["x"] if self.current_player == "X" else self.colors["o"]
            )
            
            if self.check_winner():
                messagebox.showinfo("ชนะแล้ว!", f"ผู้เล่น {self.current_player} ชนะ!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("เสมอ!", "เกมเสมอ!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        # ตรวจสอบแนวนอน
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != "":
                return True
        
        # ตรวจสอบแนวตั้ง
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True
        
        # ตรวจสอบแนวทแยง
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        
        return False
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="", fg="black", bg=self.colors["button"])
    
    def on_hover(self, button, entering):
        if button["text"] == "":
            button.config(bg=self.colors["button_hover"] if entering else self.colors["button"])

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()