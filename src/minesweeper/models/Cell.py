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
        # print(self)


    def toggle_flag(self):
        """Toggle a non revealed cell with a flag
        Add a flag on non flagged cell, remove a flag on a flagged cell.
        """
        if self.is_flagged == False:
            self.is_flagged = True
        else:
            self.is_flagged = False
                
