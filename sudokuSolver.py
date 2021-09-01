from tkinter import *
from tkinter import ttk
from time import perf_counter

class Sudoku(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        #Create all entry boxes for board GUI
        self.entries = []
        self.seperators = []
        for i in range (12):
            if (i % 4 == 0):
                self.seperators.append([])
            else:
                self.entries.append([])
            for j in range (12):
                if (i % 4 == 0):
                    s = ttk.Separator(master, orient=HORIZONTAL).grid(column=j, row=i, sticky='ew')
                    self.seperators[-1].append(s)
                elif (j % 4 == 0):
                    s = ttk.Separator(master, orient=VERTICAL).grid(column=j, row=i, sticky='ns')
                    self.seperators[-1].append(s)
                else:
                    e = Entry(master, width=5)
                    self.entries[-1].append(e)
                    e.grid(row = i, column = j, padx = 2, pady = 2, sticky = "nsew")
                    e.delete(0, END)


        #Create solve button and timer for board GUI
        self.TimerLabel = Label(master, text='0.000000 s')
        self.TimerLabel.grid(row=12, column=0, columnspan=13)
        self.SolveButton = Button(text="Solve", command=self.create_board)
        self.SolveButton.grid(row=13, column=0, columnspan=13, sticky="nsew")

    def create_board(self):
        
        #Define a blank board
        board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        self.board = board
        
        #Transfer user entries into board variable
        for i in range (9):
            for j in range (9):
                if self.entries[i][j].get() == '':
                    self.board[i][j] == 0
                else:
                    self.board[i][j] = int(self.entries[i][j].get())

        #Solve the puzzle
        t1_start = perf_counter()
        self.solve(self.board)
        t1_stop = perf_counter()
        self.TimerLabel['text'] = str(t1_stop - t1_start)
        self.display_board(self.board)
        
    def solve(self, board):
        find = self.find_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.valid(board, num, (row, col)):
                board[row][col] = num

                if self.solve(board):
                    return True

                board[row][col] = 0

        return False

    def valid(self, board, num, pos):

        # Check row
        for i in range(9):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(9):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def find_empty(self, board):
        #Returns row and column of empty cell if any exist
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j  # row, column

        return None

    def display_board(self, board):
        for i in range(9):
            for j in range(9):
                if self.entries[i][j].get() == '':
                    self.entries[i][j].insert(0, self.board[i][j])

root = Tk()
root.title("Sudoku")
root.resizable(False, False)
root.geometry("350x260")
app = Sudoku(root)

root.mainloop()
