from distutils.command.config import config
import time

from brainflow.board_shim import BoardShim,BrainFlowInputParams

import configuration

# class for board configuration
class BoardConfiguration(BrainFlowInputParams):
    serial_port = configuration.board_serial_port
    ip_port=0
    timeout = 0
    def __init__(self,
                 ip_port=configuration.board_ip_port,
                 serial_port=configuration.board_serial_port,
                 mac_address=configuration.board_mac_address,
                 other_info=configuration.other_info,
                 serial_number=configuration.board_serial_number,
                 ip_address=configuration.board_ip_address,
                 ip_protocol=configuration.board_ip_protocol,
                 timeout=configuration.board_timeout,
                 file=configuration.board_file,):
        self.ip_port = ip_port
        self.serial_port = serial_port
        self.mac_address = mac_address
        self.other_info = other_info
        self.serial_number = serial_number
        self.ip_address = ip_address
        self.ip_protocol = ip_protocol
        self.timeout = timeout
        self.file = file
 
 
 
# class for creating the board instance and perform required operations
class Board(BoardShim):
    
    _config = BoardConfiguration()
    board_id = configuration.board_id
    serial_port = _config.serial_port   
    _instance = None    
       
    @staticmethod
    def getBoard():
        if Board._instance == None:
            return Board()
        return Board._instance
    
    def __init__(self):
        super().__init__(self.board_id,self._config)
        if Board._instance != None:
            raise  Exception("This is a singleton class")
        Board._instance = self
        
    #function to start live stream
    def start_streaming(self):
        try:
        
            self.prepare_session()
            self.start_stream(2000)
            time.sleep(configuration.stream_time) #receive data for specified time
            data = self.get_board_data()
            self.stop_stream()
            print("Received data samples:",data.shape)
            return data
        except Exception as e:
            print("Error while streaming data")
            print(e)
            
        