import os

from dotenv import load_dotenv
load_dotenv()

board_ip_port=int(os.getenv("BOARD_IP_PORT"))
board_serial_port = str(os.getenv("BOARD_SERIAL_PORT"))

board_mac_address=os.getenv("BOARD_MAC_ADDRESS")
other_info=os.getenv("OTHER_INFO")
board_serial_number=os.getenv("BOARD_SERIAL_NUMBER")
board_ip_address=os.getenv("BOARD_IP_ADDRESS")
board_ip_protocol=int(os.getenv("BOARD_IP_PROTOCOL"))
board_timeout=int(os.getenv("BOARD_TIMEOUT"))
board_file=os.getenv("BOARD_FILE")
board_id = int(os.getenv("BOARD_ID"))
board_streamer_params=os.getenv("BOARD_STREAMER_PARAMS")


stream_time = int(os.getenv("STREAM_TIME"))
