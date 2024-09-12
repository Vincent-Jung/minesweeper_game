class Cell:
    def __init__(self, is_revealed: bool = False, is_flagged: bool = False, is_a_mine: bool = False, adjacent_mines: int = "", color: str=None):
        self.is_revealed = is_revealed
        self.is_flagged = is_flagged
        self.is_a_mine = is_a_mine
        self.adjacent_mines = adjacent_mines
        self.color = color
        
    def __str__(self):
        return f"Revealed: {self.is_revealed}, Flagged: {self.is_flagged}, Mine: {self.is_a_mine}, Adj mines: {self.adjacent_mines}, Color: {self.color}"
    
    def reveal_cell(self):
        """Reveal a cell on the board
        """
        self.is_revealed = True
        print(self)
        if self.is_a_mine == True:
            print("** BOOM Game over **")
            return
        elif self.adjacent_mines == 0:
            print("0 = propagate")
            self.check_cells_around()
        else:
            return self.adjacent_mines
    
    def check_cells_around(self):
        """ Check cell surrounding for propagation
        Duplicate of reveal_cell() without the mine explosion losing condition.
        Allow recursion for propagation of cell with 0 adjacent mines,
        or display mines count.
        """
        # self.is_revealed = True
        # print(self)
        if self.adjacent_mines == 0:
            self.is_revealed = True
            print("0 = propagate")
        else:
            print(self.adjacent_mines)
            return self.adjacent_mines
    
    
    def toggle_flag(self):
        """Toggle a non revealed cell with a flag
        Add a flag on non flagged cell, remove a flag on a flagged cell.
        """
        if self.is_flagged == False:
            self.is_flagged = True
        else:
            self.is_flagged = False
                
