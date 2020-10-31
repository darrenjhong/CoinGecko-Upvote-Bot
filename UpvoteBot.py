from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.coingecko.com/en/coins/yffs-finance")


for x in range (200):
	link = driver.find_element_by_link_text("👍")
	link.click()

	driver.refresh()
 