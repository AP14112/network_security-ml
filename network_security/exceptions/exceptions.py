import sys
from network_security.logging import logger
class networksecurityexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    def __str__(self):
        return f"Error occured in Script name [{self.file_name}] line number [{self.lineno}] error message [{str(self.error_message)}]"

if __name__=='__main__':
    try:
        logger.logging.info("Logging started")
        a=0/0
        print("This will not be printed")
    except Exception as e:
        raise networksecurityexception(e,sys)

