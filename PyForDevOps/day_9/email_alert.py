import shutil
import time
import logging
import datetime as dt

logging.basicConfig(filename="logs.txt",level="INFO")
print(dir(logging))
while True:
    total,used,free = shutil.disk_usage("/")

    used_per = (used / total)*100
    free_per = (free / total)*100
    if free_per < 15:
        logging.warning(str(dt.datetime.now())+"email alert sent")
    if free_per < 10:
        logging.critical("disk full")
    time.sleep(3)