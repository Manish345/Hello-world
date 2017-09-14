import logging
from selenium import webdriver
import os

import sys
sys.stdout.flush("Heeloooo Python")
sys.stdout.flush("Heeloooo Python")
sys.stdout.flush("Heeloooo Python")
sys.stdout.flush("Heeloooo Python")


driversPath = os.path.join(os.getcwd(),"\\Drivers\\chromedriver")
chromeDriverPath = os.path.normpath(driversPath)
print(chromeDriverPath)
logging.info(chromeDriverPath)

driver = webdriver.Chrome(chromeDriverPath)
#driver = webdriver.Chrome()
driver.get("http://www.google.co.in")
driver.maximize_window()

logging.basicConfig(level=logging.INFO)

print("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")
