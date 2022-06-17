import logging


class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\Abhay\\Documents\\abhay_imp\\ecommerceProject\\logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
