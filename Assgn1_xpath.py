from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://www.google.com/")

sigin = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div/div/div[2]/a")
sigin.click()
time.sleep(2)

driver.close()