from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case is started")
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(1)
driver.find_element_by_name("q").send_keys("Harman")

time.sleep(5)
driver.close()
print("test case has successfully executed")