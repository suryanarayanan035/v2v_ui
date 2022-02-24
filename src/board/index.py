import os
from brainflow.board_shim import BoardShim,BrainFlowInputParams

from dotenv import load_dotenv
load_dotenv("../.env")
class Board(BrainFlowInputParams):
    _serial_port = os.getenv("CYTON_SERIAL_PORT")
    _board_id = os.getenv("BOARD_ID")
    _instance = None
    @staticmethod
    def getBoard():
        if Board._instance == None:
            return Board()
        return Board._instance
    def __init__(self):
        if Board._instance != None:
            raise  Exception("This is a singleton class")
        Board.instance = self