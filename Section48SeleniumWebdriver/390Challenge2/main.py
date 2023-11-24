from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Main_Page")


article_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(article_number.text)
    
    
driver.close() # closes tabm
driver.quit() # closes entire browser