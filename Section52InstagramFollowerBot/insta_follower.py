from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
SIMILAR_ACCOUNT = "potus"
INSTA_EMAIL = config("insta_email")
INSTA_PASSWORD = config("insta_password")

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.followers = []
        
    def login(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(1)
        self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTA_EMAIL)
        self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTA_PASSWORD)
        self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, value='//button[text()="Save Info"]').click()
        time.sleep(2)
    
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
        
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()