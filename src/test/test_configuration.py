import unittest
import configuration
class TestConfiguration(unittest.TestCase):
    def test_environmentvariables(self):
        board_id = configuration.board_id
        assert board_id == 0
        assert type(board_id) == int
        
if __name__ == "__main__":
    unittest.main()