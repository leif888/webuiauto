from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.leafground.com/menu.xhtml?i=0")

driver.find_element(By.CLASS_NAME, 'ui-menuitem-text').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'New').click()

driver.find_element(By.PARTIAL_LINK_TEXT, 'Members').click()

sleep(4)
