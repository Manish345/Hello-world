import logging
from selenium import webdriver
import os, sys

driversPath = os.path.join(os.getcwd(),"\\Users\\manish2\\source\\Hello-world\\Drivers\\chromedriver")
#driversPath = os.path.join(os.getcwd(),"\\Drivers\\chromedriver")
chromeDriverPath = os.path.normpath(driversPath)
print(chromeDriverPath)
logging.info(chromeDriverPath)

driver = webdriver.Chrome(chromeDriverPath)
driver.get("http://www.google.co.in")
driver.maximize_window()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

print("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")
