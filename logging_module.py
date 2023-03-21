import logging

logger = logging.getLogger('PythonPRO_vol2')
logger.setLevel(logging.INFO)

ch = logging.FileHandler('Student_add_logging')
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info('adding students to the group')

