import os

from dotenv import load_dotenv
load_dotenv()

board_id = int(os.getenv("BOARD_ID"))
cyton_serial_port = os.getenv("CYTON_SERIAL_PORT")
