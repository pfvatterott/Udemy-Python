from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://www.python.org/")


events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')

event_dictionary = {}
for n in range(len(events)):
    event_dictionary[n] = {
        'time': events[n].find_element(By.CSS_SELECTOR, value="time").text,
        'name': events[n].find_element(By.CSS_SELECTOR, value="a").text
    }

    

print(event_dictionary)
    
    
driver.close() # closes tabm
driver.quit() # closes entire browser