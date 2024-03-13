from nextlog import Logger
import logging

labels = {
    'job' : 'localhost-6'
}

loki_url = "http://localhost:3100/api/prom/push"

logger = Logger(name="my_logger",level=logging.DEBUG,loki_url=loki_url,labels=labels)

logger.debug("DEBUG log test 0")
logger.warning("WARNING log test 0")
logger.error("INFO log test 0")
logger.critical("CRITICAL log test 0")