import logging
from selenium import webdriver
import os, sys, pytest

root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
formatter = logging.Formatter('%(asctime)s:%(levelname)s: %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

driversPath = os.path.join(os.getcwd(),"Drivers\\chromedriver")
chromeDriverPath = os.path.normpath(driversPath)
print(chromeDriverPath)

# driver = webdriver.Chrome(chromeDriverPath)
# driver.get("http://www.google.co.in")
# driver.maximize_window()
logging.info("Running Selenium code")
logging.info("GitHUb is working fine with Jenkins")

