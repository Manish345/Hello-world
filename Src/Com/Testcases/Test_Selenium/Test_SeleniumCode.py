# from selenium import webdriver
import os
# 
# driversPath = os.path.join(os.getcwd(),"..\\..\\Drivers\\chromedriver")
# chromeDriverPath = os.path.normpath(driversPath)
# print(chromeDriverPath)
# 
# driver = webdriver.Chrome(chromeDriverPath)
# driver.get("http://www.google.co.in")
# driver.maximize_window()
# while(1):
#     pass
pathval = os.getcwd() 
print(pathval)
print(os.path.abspath(pathval))