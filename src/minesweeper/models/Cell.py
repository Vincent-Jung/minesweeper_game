class Cell:
    def __init__(self, is_revealed: bool = False, is_flagged: bool = False, is_a_mine: bool = False, adjacent_mines: int = ""):
        self.is_revealed = is_revealed
        self.is_flagged = is_flagged
        self.is_a_mine = is_a_mine
        self.adjacent_mines = adjacent_mines
        
    def __str__(self):
        return f"Revealed: {self.is_revealed}, Flagged: {self.is_flagged}, Mine: {self.is_a_mine}, Adj mines: {self.adjacent_mines}"
    
    def reveal_cell(self):
        """Reveal a cell on the board
        """
        self.is_revealed = True
        print(self)
        if self.is_a_mine == True:
            print("** BOOM Game over **")
    
    def toggle_flag(self):
        """Toggle a non revealed cell with a flag
        Add a flag on non flagged cell, remove a flag on a flagged cell.
        """
        if self.is_flagged == False:
            self.is_flagged = True
        else:
            self.is_flagged = False
        
    def calculate_number(self):
        pass
        

        # Tests
cA1 = Cell(False, False, False, 1)  # no Mine
cA2 = Cell(False, False, True, 1)  # Mine !
cA3 = Cell(False, True, False, 1)

# print(cA1)
# cA1.reveal_cell()
# cA2.reveal_cell()

