import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name):%(threadname)s:%(process)s:%(message)s'
root_logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,format=fmt_str,filename='threadLog')

root_logger.name='snapdragon'
logging.debug('debug message')
logging.info('a confirmation message')
#logging.warn('warning note')
logging.error('error')