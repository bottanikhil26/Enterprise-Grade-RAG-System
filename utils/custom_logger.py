import os
import sys
import logging
from datetime import datetime



class CustomLogger:
    def __init__(self):
        self.LOG_DIR = os.path.join(os.getcwd(),"logs")
        os.makedirs(self.LOG_DIR,exist_ok=True)
        LOG_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        
        log_file_path=os.path.join(self.LOG_DIR,LOG_file)

        logging.basicConfig(
            filename=log_file_path,
            format="[%(asctime)s] %(levelname)s - %(name)s - (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )
    def get_logger(self,name=__file__):
        return logging.getLogger(os.path.basename(name))
    


