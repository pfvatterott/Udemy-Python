from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from decouple import config
import time


tinder_url = "https://tinder.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(tinder_url)

time.sleep(1)
driver.find_element(By.LINK_TEXT, value="Log in").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, value="iframe[title='Sign in with Google Button']").click()

google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
print(driver.title)

driver.find_element(By.CSS_SELECTOR, value="input[aria-label='Email or phone']").send_keys('pvatt256@gmail.com')
driver.find_element(By.XPATH, value='//*[@id="identifierNext"]/div/button').click()