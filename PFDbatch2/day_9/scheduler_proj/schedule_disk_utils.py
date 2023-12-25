import shutil
import logging
import schedule

logging.basicConfig(filename="logs.txt",level="INFO",)
def check_disk():
    disk = shutil.disk_usage("/")
    per_used = (disk.total - disk.free)/disk.total*100
    if per_used > 75:
        logging.warning("disk full")
    elif per_used > 95:
        logging.critical("critical disk full")


schedule.every(1).day.do(check_disk) #cron setup

while True:
    schedule.run_pending()