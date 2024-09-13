import pytest
from minesweeper.models.Board import Board
from minesweeper.models.Cell import Cell
from minesweeper.models.GameState import GameState

class TestCell:
    def test_toggle_flag(self):
        cell = Cell()
        assert not cell.is_flagged  # Initially, the cell should not be flagged
        cell.toggle_flag()
        assert cell.is_flagged  # After toggling, the cell should be flagged
        cell.toggle_flag()
        assert not cell.is_flagged  # Toggling again should remove the flag

class TestBoard:
    def test_generate_board(self):
        board = Board(difficulty="custom", rows=3, columns=3, mines=2)
        board.generate_board()
        assert len(board.cells) == 3  # Check the number of rows
        assert len(board.cells[0]) == 3  # Check the number of columns

    def test_distribute_random_mines(self):
        board = Board(difficulty="easy")
        board.generate_board()
        mine_count = sum(cell.is_a_mine for row in board.cells for cell in row)
        assert mine_count == 10  # Ensure exactly 10 mines were placed

class TestGameState:
    def test_initialize(self):
        game_state = GameState()
        game_state.initialize(difficulty="easy")
        assert game_state.board is not None  # The board should be initialized
        assert game_state.board.difficulty == "easy"

    def test_trigger_victory(self):
        game_state = GameState()
        game_state.initialize(difficulty="easy")
        # Set up a winning condition (all mines flagged, all non-mines revealed)
        for row in game_state.board.cells:
            for cell in row:
                if cell.is_a_mine:
                    cell.is_flagged = True
                else:
                    cell.is_revealed = True
        assert game_state.trigger_victory()  # Should return True
