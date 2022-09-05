from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# # Home work! It is work but it hardcode :(
driver = webdriver.Chrome()
url = 'https://github.com/login'
driver.get(url)

elem =driver.find_element(By.ID,"login_field")
elem.send_keys("yukyuiyujhuuiiy8877")
elemp= driver.find_element(By.ID, "password")
elemp.send_keys("yukyuiyujhuuiiy8877")
elemp.send_keys(Keys.ENTER)
driver.implicitly_wait(2)
assert driver.find_element(By.ID, 'js-flash-container').is_displayed() == True
assert  driver.find_element(By.ID, 'js-flash-container').text == 'Incorrect username or password.' #Homework v2
driver.close()



