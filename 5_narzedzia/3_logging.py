import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

# konfiguracja formatowania
logging.basicConfig(
    format='%(asctime) - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:S %p',
    level=logging.INFO
)

logger = logging.getLogger('Moja apka')
logger.info('To jest informacja')

