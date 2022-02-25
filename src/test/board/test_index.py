import unittest
from src.board.index import Board 

import configuration

class TestBoard(unittest.TestCase):
    
    def test_parameters(self):
        board1 = Board()
        assert board1.serial_port == configuration.cyton_serial_port
        board1.board_id = 8
        assert board1.board_id != configuration.board_id
        
    def test_if_exception_raises_on_multiple_constructor_call(self):
        with self.assertRaises(Exception):
            Board()
            Board()
            