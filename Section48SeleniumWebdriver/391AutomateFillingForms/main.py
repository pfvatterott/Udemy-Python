from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


# driver.get("https://en.wikipedia.org/wiki/Main_Page")


# # article_number = driver.find_element(By.NAME, value='search') 
# # # article_number.click()

# # anyone_can_edit_link = driver.find_element(By.LINK_TEXT, "anyone can edit")
# # anyone_can_edit_link.click()

# driver.find_element(By.NAME, value='search').send_keys("Python")
# driver.find_element(By.NAME, value='search').send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Paul")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Vatt")

email = driver.find_element(By.NAME, value="email")
email.send_keys("test@test.com")

button = driver.find_element(By.CSS_SELECTOR, value='form button')
button.click()

# driver.close() # closes tab
# driver.quit() # closes entire browser  