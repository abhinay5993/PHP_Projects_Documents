from selenium import webdriver
from selenium.webdriver.support.select import Select

browserDriver=webdriver.Chrome(executable_path='./driverLoc/chromedriver')

browserDriver.get('https://www.amazon.in/')
browserDriver.maximize_window()
browserDriver.implicitly_wait(30)
items=Select(browserDriver.find_element_by_xpath("//select[@aria-describedby='searchDropdownDescription']"))
print("\ndata szie : ",len(items.options))
for data in items.options:
    print("\nData Items : ",data.text)


browserDriver.quit()
print("\nBrowser Closed!!!..No of Items : ")