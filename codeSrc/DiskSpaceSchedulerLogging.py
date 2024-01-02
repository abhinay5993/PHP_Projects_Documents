import math
import shutil as sht
import logging as lg
import time
import schedule as sch

lg.basicConfig(format="%(asctime)s - %(levelname)s : %(message)s",filename='codeSrc/deskSpaceNotes.log',datefmt='%d-%m-%Y %I:%M:%S %p %Z',level=lg.INFO)
def checkDiskSpace():
    diskSize=sht.disk_usage("/")
    usedPercent=round((diskSize.total-diskSize.free)*100/diskSize.total)
    print(f"\nDisk is used by : {usedPercent}%")
    if usedPercent>75:
         lg.warning("Disk will be soon get FilledUp.")
    elif usedPercent>95:
         lg.critical("Disk space is in critical!! state.")
    else:
         lg.info("Disk is in healthy with "+str(usedPercent)+"%")
"""
Setting up the cron scheduler
"""
sch.every(20).seconds.do(checkDiskSpace)

"""
Execute the scheduler
"""
while True:
    sch.run_pending()
    time.sleep(1)
