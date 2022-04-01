'''
Created on 15-Aug-2021

@author: abhinay
'''

from selenium import webdriver
browserDriver=webdriver.Chrome(executable_path='/home/abhinay/Documents/eclipseLocalWorksExps/TestMyPythonExpApps/driverSrc/chromedriver')
browserDriver.get('https:\\www.youtube.com')
print('\nFetched Cookies : ',browserDriver.get_cookies())
browserDriver.maximize_window()
browserDriver.implicitly_wait(30)
browserDriver.quit()
print("\nBrowser Closed!!!")
