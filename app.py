from source.ml_project.logger import logging
from source.ml_project.exception import CustomException
import sys



if __name__=='__main__':
    logging.info("Logging has started")



    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

