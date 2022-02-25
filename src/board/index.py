import os
from brainflow.board_shim import BoardShim,BrainFlowInputParams

import configuration

class Board(BrainFlowInputParams):
    serial_port = configuration.cyton_serial_port
    board_id = configuration.board_id
    _instance = None
    
    @staticmethod
    def getBoard():
        if Board._instance == None:
            return Board()
        return Board._instance
    
    def __init__(self):
        if Board._instance != None:
            raise  Exception("This is a singleton class")
        Board._instance = self