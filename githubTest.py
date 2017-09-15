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

# logging.basicConfig(level=logging.INFO)
# stderrLogger=logging.StreamHandler()
# stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
# logging.getLogger().addHandler(stderrLogger)


root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logg = root.addHandler(ch)

root.info("GitHUb is working fine")
root.info("GitHUb is working fine")
root.info("GitHUb is working fine")
root.info("GitHUb is working fine")

logg.info("GitHUb Loggs is working fine")
logg.info("GitHUb Loggs is working fine")
logg.info("GitHUb Loggs is working fine")

print("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")
logging.info("GitHUb is working fine")

