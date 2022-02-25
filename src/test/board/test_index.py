import unittest
from src.board.index import Board 

import configuration

class TestBoard(unittest.TestCase):
    
    def test_if_exception_raises_on_multiple_constructor_call(self):
        with self.assertRaises(Exception):
            Board()
            Board()
            
    def test_streaming(self):
        board =  Board.getBoard()
        board.start_streaming()
            