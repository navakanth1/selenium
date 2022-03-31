from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

value = input("Enter the product name to be searched")
print("test started")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys(value)
driver.find_element_by_class_name("L0Z3Pu").click()
time.sleep(5)
driver.close()
print("test completed")