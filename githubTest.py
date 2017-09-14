import logging
from selenium import webdriver
import os

driversPath = os.path.join(os.getcwd(),"\\Drivers\\chromedriver")
chromeDriverPath = os.path.normpath(driversPath)
print(chromeDriverPath)

driver = webdriver.Chrome(chromeDriverPath)
#driver = webdriver.Chrome()
driver.get("http://www.google.co.in")
driver.maximize_window()

logging.basicConfig(level=logging.INFO)

print("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")
