import time
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# drpdwn = Select(driver.find_element(By.ID,"dropdown-class-example"))
# time.sleep(1)
# drpdwn.select_by_value('option2')
# drpdwn.select_by_index(3)
# drpdwn.select_by_visible_text("Option1")


# chckbx = driver.find_element(By.XPATH,"//input[@value='option3']")
# chckbx.click()
# if chckbx.is_selected():
#   print ('option 3 is selected')


# rdbtn = driver.find_element(By.XPATH,"//input[@name='radioButton']")
# rdbtn.click()

time.sleep(3)

driver.close()
