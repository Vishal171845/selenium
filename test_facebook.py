from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
username = input(print("enter the username"))
password = input(print("enter the password"))

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case is started")
driver.maximize_window()
driver.get("https://www.facebook.com/login/")
time.sleep(2)
driver.find_element_by_name("email").send_keys("username")
time.sleep(2)
driver.find_element_by_name("pass").send_keys("password")
time.sleep(2)
driver.find_element_by_name("login").click()

time.sleep(2)
driver.close()
print("test case has successfully executed")