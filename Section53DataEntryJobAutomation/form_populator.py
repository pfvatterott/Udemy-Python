from selenium import webdriver
from selenium.webdriver.common.by import By
from decouple import config
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfIrUyNCN6FqOjEaKyaLIVBM_5iPwZgFVx7Aig-5Bj6ckCEKA/viewform?usp=sf_link"

class FormPopulator:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        
    def open_form(self):
        self.driver.get(FORM_URL)
        time.sleep(1)
        
    def populate_form(self, property):
        self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(property['address'])
        self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(property['price'])
        self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(property['link'])
        self.driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        
    def reload_form(self):
        self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
        time.sleep(1)