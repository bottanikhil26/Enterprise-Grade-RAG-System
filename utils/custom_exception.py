import os
import traceback
import sys      

class CustomException(Exception):
    def __init__(self,error_message:str,error_detail:sys):
        _,_,exc_tb = error_detail.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno
        self.error_message =str(error_message)

        self.traceback_str = ''.join(traceback.format_exception(*error_detail.exc_info()))

    def __str__(self):
        return f"""
        Error Occurred in script : {self.file_name}
        at line number : {self.line_number}
        Error Message : {self.error_message}
        Traceback Details : {self.traceback_str}
        """