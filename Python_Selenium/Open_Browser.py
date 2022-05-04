from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("D:\Automation\Chrome Driver\chromedriver.exe")
driver.get("https://stg.ciceroni.in/ahmedabad")
driver.find_element(By.XPATH, "/html/body/app-root/div[1]/app-home/search/div/div/div/div[1]/select").click()
driver.find_element(By.XPATH, "/html/body/app-root/div[1]/app-home/search/div/div/div/div[1]/select/option[3]").click()
city_select = "/html/body/app-root/div[1]/app-home/search/div/div/div/div[1]/select/option[3]"
new = city_select.
print(new.text)
