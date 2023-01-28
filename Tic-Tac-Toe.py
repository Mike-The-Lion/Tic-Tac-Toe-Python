import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk() # main window
        self.root.title("Tic Tac Toe")  # title of the window
        self.root.resizable(width=False, height=False)  # window size is fixed
        self.create_widgets()   # create widgets
        self.player = "X"   # player X starts first
        self.game_mode = "VS A.I"  # "Two Players" or "VS A.I"

    def create_widgets(self):   # create widgets
        self.buttons = []   # list of buttons
        for i in range(9):  # create 9 buttons
            button = tk.Button(self.root, width=5, height=2, font=("Helvetica", 24),    # button properties
                               command=lambda i=i: self.on_button_press(i)) # lambda function to pass index
            button.grid(row=i // 3, column=i % 3)   # grid layout
            self.buttons.append(button) # add button to the list

        self.game_mode_var = tk.StringVar(value="Two Players")  # "Two Players" or "VS A.I"
        self.game_mode_var.trace("w", self.on_game_mode_change) # trace changes in the variable
        self.pvp_button = tk.Radiobutton(self.root, text="Two Players", variable=self.game_mode_var, value="Two Players")   
        self.pvp_button.grid(row=3, column=3, sticky="w")   
        self.pve_button = tk.Radiobutton(self.root, text="VS A.I", variable=self.game_mode_var, value="VS A.I")    
        self.pve_button.grid(row=3, column=4, sticky="w")

        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart)      
        self.restart_button.grid(row=4, column=3, columnspan=2, sticky="nsew")
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=5, column=3, columnspan=2, sticky="nsew")

    def on_button_press(self, index):   # called when a button is pressed
        button = self.buttons[index]    # get the button
        if button["text"] == "":    # if the button is empty   
            button.config(text=self.player) # set the text to the current player
            if self.check_winner(): # check if the player won
                messagebox.showinfo("Winner", f"Player {self.player} won the game!")    # show a message box
            elif self.check_draw(): # check if it's a draw
                messagebox.showinfo("Draw", "It's a draw!") # show a message box
            else:
                self.player = "O" if self.player == "X" else "X"    # change the player
                if self.game_mode == "VS A.I" and self.player == "O":   # if the game mode is VS A.I and it's the AI's turn
                    self.ai_move()  # make the AI move

    def check_winner(self): # check if the current player won
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combination in winning_combinations:    # check all winning combinations
            if all(self.buttons[i]["text"] == self.player for i in combination):
                return True
        return False

    def check_draw(self):   # check if it's a draw
        return all(button["text"] != "" for button in self.buttons)

    def on_game_mode_change(self, *args):   # called when the game mode is changed
        self.game_mode = self.game_mode_var.get()   # get the game mode
        if self.game_mode == "VS A.I":  # if the game mode is VS A.I
            self.ai_move()  

    def ai_move(self):  # make the AI move
        empty_buttons = [i for i in range(9) if self.buttons[i]["text"] == ""]  
        if empty_buttons:
            ai_choice = random.choice(empty_buttons)    # choose a random empty button   
            self.buttons[ai_choice].config(text="O")    
            if self.check_winner(): # check if the AI won
                messagebox.showinfo("Winner", "AI won the game!")
            elif self.check_draw(): # check if it's a draw
                messagebox.showinfo("Draw", "It's a draw!")
            else:
                self.player = "X"   

    def restart(self):  # restart the game
        for button in self.buttons: # clear all buttons
            button.config(text="")  
        self.player = "X"   # player X starts first

if __name__ == "__main__":  # if the file is run directly
    game = TicTacToe()  # create a game object
    game.root.mainloop()    # start the main loop

