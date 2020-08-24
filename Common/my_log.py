
import logging


class MyLog:

    def my_log(self,msg,level):

        my_logger = logging.getLogger('UI')
        my_logger.setLevel('DEBUG')

        formater = ''

        sh = logging.StreamHandler()
        sh.setLevel('DEBUG')
        sh.setFormatter(formater)

        fh = logging.FileHandler(r'C:\Users\issuser\Desktop\UI_AUTO\Common\log.txt',encoding='utf-8')
        fh.setLevel('DEBUG')
        sh.setFormatter(formater)

        my_logger.addHandler(sh)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)

        my_logger.removeHandler(sh)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')
