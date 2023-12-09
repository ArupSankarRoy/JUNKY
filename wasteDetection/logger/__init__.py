
# When I run app.py 1st ly a folder called log is created.Inside that folder, There exist two folder,
# They are responsible for containing the information about your run


import logging
import os
from datetime import datetime
from from_root import from_root


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # with .log extension
log_path = os.path.join(from_root() ,'log', LOG_FILE)

os.makedirs(log_path , exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path , LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)