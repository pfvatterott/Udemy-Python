from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from decouple import config
import time

linkedIn_username = config("linkedIn_username")
linkedIn_password = config("linkedIn_password")
phone = config("phone")
linkedIn_url = "https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D3770815303%26distance%3D25%26f_AL%3Dtrue%26f_WT%3D2%26geoId%3D103644278%26keywords%3Dsuccess%2520engineer%26origin%3DJOB_SEARCH_PAGE_JOB_FILTER%26refresh%3Dtrue%26sortBy%3DR&trk=public_jobs_nav-header-signin"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(linkedIn_url)


# Login
driver.find_element(By.XPATH, value='//*[@id="username"]').send_keys(linkedIn_username)
driver.find_element(By.XPATH, value='//*[@id="password"]').send_keys(linkedIn_password)
driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button').click()

# Wait 3 seconds
time.sleep(3)

# Create list of jobs
job_list = driver.find_elements(By.CSS_SELECTOR, value='ul li div .job-card-list__entity-lockup')


for job in job_list:
    job.click()

    time.sleep(1)

    # clicks easy apply button
    try: 
        driver.find_element(By.CLASS_NAME, value="jobs-apply-button").click()
    except NoSuchElementException:
        pass
    else:  

        time.sleep(1)

        # clicks next button
        driver.find_element(By.CSS_SELECTOR, value="footer div button").click()

        time.sleep(1)

        try:
            driver.find_element(By.CSS_SELECTOR, value="button[aria-label='Review your application']").click()
        except NoSuchElementException:
            driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, value=".artdeco-modal__actionbar .artdeco-button--secondary").click()
            time.sleep(1)
        else:
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, value="label[for='follow-company-checkbox']").click()
            driver.find_element(By.CLASS_NAME, value="artdeco-button--primary").click()
            time.sleep(1)
            try:
                driver.find_element(By.CSS_SELECTOR, value="button[aria-label='Dismiss']").click()
            except NoSuchElementException:
                pass
        
    




# driver.close() # closes tab
# driver.quit() # closes entire browser  