import tkinter as tk

initBoard = [["1", "2", "3"],
             ["4", "5", "6"], 
             ["7", "8", "9"]]

BOARD = [["1", "2", "3"],
         ["4", "5", "6"], 
         ["7", "8", "9"]]

currentPlayer = 0
isFinished = False

def GetColOfBoard(_move):
    _col = (_move - 1) % 3
    return _col

def GetRowOfBoard(_move):
    if(_move == 1 or _move == 2 or _move == 3):
        _row = 0
    elif (_move == 4 or _move == 5 or _move == 6):
        _row = 1
    else:
        _row = 2
    return _row

def IsValidMove(_row, _col, _board): 
    if _board[_row][_col] == initBoard[_row][_col]:
        return True
    else:
        return False

def CheckBoard(_board):
    
    if(    _board[0][0] == _board[0][1] == _board[0][2]    ### Top
        or _board[1][0] == _board[1][1] == _board[1][2]    ### Middle
        or _board[2][0] == _board[2][1] == _board[2][2]    ### Bottom
        or _board[0][0] == _board[1][0] == _board[2][0]    ### Left
        or _board[0][1] == _board[1][1] == _board[2][1]    ### Centre
        or _board[0][2] == _board[1][2] == _board[2][2]    ### Right
        or _board[0][0] == _board[1][1] == _board[2][2]    ### Left to right \
        or _board[0][2] == _board[1][1] == _board[2][0]):  ### Right to left /
    
        return True