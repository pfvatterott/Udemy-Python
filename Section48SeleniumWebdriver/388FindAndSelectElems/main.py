from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
# driver.get("https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(price_dollar)
# print(price_cents)


driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
button = driver.find_element(By.ID, value="submit")
driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
driver.find_elements(By.CSS_SELECTOR, value=".documentation-widget a")

bottom_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[3]/ul/li[8]/a').text

# driver.close() # closes tab
driver.quit() # closes entire browser