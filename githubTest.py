import logging
from selenium import webdriver
import os, sys, pytest

# driversPath = os.path.join(os.getcwd(),"\\Users\\manish2\\source\\Hello-world\\Drivers\\chromedriver")
driversPath = os.path.join(os.getcwd(),"Drivers\\chromedriver")
chromeDriverPath = os.path.normpath(driversPath)
print(chromeDriverPath)
logging.info(chromeDriverPath)

# driver = webdriver.Chrome(chromeDriverPath)
# driver.get("http://www.google.co.in")
# driver.maximize_window()
# print("Running Selenium code")

logging.basicConfig(level=logging.INFO)
stderrLogger=logging.StreamHandler()
stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(stderrLogger)

print("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")

pytest.main(["-s","githubTest.py"])
