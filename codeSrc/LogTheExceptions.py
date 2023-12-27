import datetime
import logging as lg

lg.basicConfig(format="%(asctime)s - %(levelname)s : %(message)s",filename='codeSrc/myExecLogger.log',datefmt='%d-%m-%Y %I:%M:%S %p %Z',level=lg.DEBUG)
lgObj=lg.getLogger()
lgObj.warning("I am giving worning!! with warning() ")
lgObj.info("Show use of existing str(dir(lgObj)) functions from log info() : ")
lgObj.debug("I am in debug() mode , please analyze it..")
lgObj.error("This will be Error!!...please log using error() ")
lgObj.critical("I am very critical!! .. you have fix with .. critical()..")