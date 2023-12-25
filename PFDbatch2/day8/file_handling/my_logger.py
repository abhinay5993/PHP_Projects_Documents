import logging

logging.basicConfig(format="%(asctime)s %(message)s",filename='my_logs.log',datefmt='%d/%m/%Y %I:%M:%S %p',level=logging.DEBUG)
print(dir(logging))
logging = logging.getLogger()
print(dir(logging))

logging.debug("This is a debug message")
logging.info("this is fine")

logging.warning("this may break")

logging.error("This is an error, fix it")

logging.critical("This is a critical error, fix it")