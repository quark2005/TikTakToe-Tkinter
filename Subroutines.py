import tkinter as tk
import BoardCode as bc

def CharacterLimit(entry_text, limit):
    if len(entry_text.get()) > limit:
        entry_text.set(entry_text.get()[:-1])

def CharacterSizeLimitForMove(_entryText):
    if len(_entryText.get()) > 1:
        if ord(_entryText.get()[1]) < 49 or ord(_entryText.get()[1]) > 57:
            _entryText.set(_entryText.get()[0])
        else:
            _entryText.set(_entryText.get()[1])

def CharacterLimitToDigitForMove(_entryText):
    if len(_entryText.get()) == 1:
        if ord(_entryText.get()) < 49 or ord(_entryText.get()) > 57:
            if len(_entryText.get()) == 1:
                _entryText.set("")
            else:
                _entryText.set(1)

def GameInit(_root, _player1Name, _player2Name):
    board = bc.BOARD

    ClearFrame(_root)
    InfoFrameInit(_root, board, _player1Name, _player2Name)
    BoardDraw(_root, board)

def ClearFrame(_frame):
   for widgets in _frame.winfo_children():
      widgets.destroy()

def InfoFrameInit(_root, _board, _player1Name, _player2Name):
    
    leftFrame = tk.Frame(_root, bg="white", width=350, height=400).grid(row=0, column=0, rowspan=2, padx=50, pady=50)

    infoFrame = tk.Frame(leftFrame, bg="white", width=300, height=630)
    infoFrame.pack_propagate(False)
    infoFrame.grid(row=0, column=0, padx=50, pady=10)

    if _player1Name == "":
        _player1Name = "Naughts"
    if _player2Name == "":
        _player2Name = "Crosses"

    player1LabelText = "NAUGHTS = " + _player1Name
    player2LabelText = "CROSSES = " + _player2Name

    player1Label = tk.Label(infoFrame, bg="white", text=player1LabelText, font=10).grid(row=0, column=0, padx=10, pady=10)
    player2Label = tk.Label(infoFrame, bg="white", text=player2LabelText, font=10).grid(row=1, column=0, padx=10, pady=10)

    moveEnterFrame = tk.Frame(leftFrame, bg="white")
    moveEnterFrame.pack_propagate(False)
    moveEnterFrame.grid(row=1, column=0, padx=50, pady=10)

    moveID = tk.StringVar()
    moveEntryBoxLabel = tk.Label(moveEnterFrame, bg="white", text="Enter Move 1-9", font=20).grid(row=2, column=0, padx=5, pady=10)
    moveEntryBox = tk.Entry(moveEnterFrame, textvariable=moveID, bg="navajo white", font=20).grid(row=2, column=1, padx=10, pady=10, ipadx=2, ipady=2)
    moveID.trace("w", lambda *args: CharacterSizeLimitForMove(moveID))
    moveID.trace("w", lambda *args: CharacterLimitToDigitForMove(moveID))

    enterMoveButton = tk.Button(moveEnterFrame, text="ENTER MOVE", command=lambda *args: EnterMove(moveID.get(), _root, _board, moveEnterFrame), height=2, width=40)
    enterMoveButton.grid(row=3, column=0, columnspan=2, padx=5, pady=10)


def EnterMove(str_move, _root, _board, _moveEnterFrame, _infoFrame):
    if str_move != "":
        move = int(str_move)
        row = bc.GetRowOfBoard(move)
        col = bc.GetColOfBoard(move)

        if bc.IsValidMove(row, col, _board) == True:
            if bc.currentPlayer == 0:
                _board[row][col] = "O"
                BoardDraw(_root, _board)
            else:
                _board[row][col] = "X"
                BoardDraw(_root, _board)
            bc.currentPlayer = (bc.currentPlayer + 1) % 2

        if bc.CheckBoard(_board) == True:
            bc.currentPlayer = (bc.currentPlayer + 1) % 2
            GameOver(_root, _moveEnterFrame, bc.currentPlayer, _infoFrame)

def GameOver(_root, _moveEnterFrame, _winner, _infoFrame):
    ClearFrame(_moveEnterFrame)



    print(_winner)

def BoardDraw(_root, _board):
    boardFrame = tk.Frame(_root, bg="BLACK", width=630, height=630)
    boardFrame.grid(row=0, column=1, rowspan=2, columnspan=2 ,padx=50, pady=50)

    topLeftFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    topLeftFrame.pack_propagate(False)
    topLeftFrame.grid(row=0, column=0, padx=10, pady=10)
    topLeftFrameData = tk.Label(topLeftFrame, bg="white", text=_board[0][0], font=("Arial", 20)).pack(padx=10, pady=30)

    topCentreFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    topCentreFrame.pack_propagate(False)
    topCentreFrame.grid(row=0, column=1, padx=5, pady=5)
    topCentreFrameData = tk.Label(topCentreFrame, bg="white", text=_board[0][1], font=("Arial", 20)).pack(padx=10, pady=30)

    topRightFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    topRightFrame.pack_propagate(False)
    topRightFrame.grid(row=0, column=2, padx=10, pady=10)
    topRightFrameData = tk.Label(topRightFrame, bg="white", text=_board[0][2], font=("Arial", 20)).pack(padx=10, pady=30)

    middleLeftFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    middleLeftFrame.pack_propagate(False)
    middleLeftFrame.grid(row=1, column=0, padx=10, pady=5)
    middleLeftFrameData = tk.Label(middleLeftFrame, bg="white", text=_board[1][0], font=("Arial", 20)).pack(padx=10, pady=30)


    middleCentreFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    middleCentreFrame.pack_propagate(False)
    middleCentreFrame.grid(row=1, column=1, padx=5, pady=5)
    middleCentreFrameData = tk.Label(middleCentreFrame, bg="white", text=_board[1][1], font=("Arial", 20)).pack(padx=10, pady=30)

    middleRightFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    middleRightFrame.pack_propagate(False)
    middleRightFrame.grid(row=1, column=2, padx=10, pady=5)
    middleRightFrameData = tk.Label(middleRightFrame, bg="white", text=_board[1][2], font=("Arial", 20)).pack(padx=10, pady=30)

    bottomLeftFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    bottomLeftFrame.pack_propagate(False)
    bottomLeftFrame.grid(row=2, column=0, padx=10, pady=10)
    bottomLeftFrameData = tk.Label(bottomLeftFrame, bg="white", text=_board[2][0], font=("Arial", 20)).pack(padx=10, pady=30)

    bottomCentreFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    bottomCentreFrame.pack_propagate(False)
    bottomCentreFrame.grid(row=2, column=1, padx=5, pady=5)
    bottomCentreFrameData = tk.Label(bottomCentreFrame, bg="white", text=_board[2][1], font=("Arial", 20)).pack(padx=10, pady=30)

    bottomRightFrame = tk.Frame(boardFrame, bg="light grey", width=100, height=100)
    bottomRightFrame.pack_propagate(False)
    bottomRightFrame.grid(row=2, column=2, padx=10, pady=10)
    bottomRightFrameData = tk.Label(bottomRightFrame, bg="white", text=_board[2][2], font=("Arial", 20)).pack(padx=10, pady=30)


