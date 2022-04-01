from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

browserDriver=webdriver.Chrome(executable_path='./driverLoc/chromedriver')
browserDriver.get('https:\\www.youtube.com')
browserDriver.set_page_load_timeout(2)
print('\nFetched Cookies : ',browserDriver.get_cookies())
browserDriver.maximize_window()

browserDriver.get("https://www.youtube.com/c/Telusko/playlists")

#implicit wait
#browserDriver.implicitly_wait(30)

#explicit wait
print("\nApplying Explicit waits!!!...")
wt=WebDriverWait(browserDriver,15)
print("\nAttribute value : ",browserDriver.find_element_by_xpath("//yt-formatted-string[contains(text(),'Website')]").get_attribute('class'))
xpy="(//div[@class='tab-content style-scope tp-yt-paper-tab'])[7]"
wt.until(expected_conditions.presence_of_element_located(By.XPATH,xpy))
browserDriver.find_element_by_xpath(xpy).click()
print("\nClicked on Course!!!!...")

browserDriver.quit()
print("\nBrowser Closed!!!")
