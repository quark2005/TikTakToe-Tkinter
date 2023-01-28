import tkinter as tk
import Subroutines as sub

root = tk.Tk()
root.title("TICK TACK TOE")
root.geometry("1000x1000")
root.resizable(False, False)


menuFrame = tk.Frame(root)
menuFrame.grid(row=0, column=0, padx=10, pady=10)

player1Name = tk.StringVar()
labelPlayer1Input = tk.Label(menuFrame, text="Enter Player 1 Name:").grid(row=0, column=0, padx=0, pady=0)
player1NameEntry = tk.Entry(menuFrame, textvariable=player1Name).grid(row=0, column=1, padx=5, pady=10)
player1Name.trace("w", lambda *args: sub.CharacterLimit(player1Name, 10))

player2Name = tk.StringVar()
labelPlayer2Input = tk.Label(menuFrame, text="Enter Player 2 Name:").grid(row=1, column=0, padx=0, pady=0)
player2NameEntry = tk.Entry(menuFrame, textvariable=player2Name).grid(row=1, column=1, padx=5, pady=10)
player2Name.trace("w", lambda *args: sub.CharacterLimit(player2Name, 10))

startButton = tk.Button(menuFrame, text="Start", command=lambda *args: sub.GameInit(root, player1Name.get(), player2Name.get()))
startButton.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()