from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case is started")
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)
driver.find_element_by_name("username").send_keys("jdhjdjjbdnmj")
time.sleep(2)
driver.find_element_by_name("Password").send_keys("hsgsj")
time.sleep(2)
driver.find_element_by_name(" "),click()

time.sleep(5)
driver.close()
print("test case has successfully executed")