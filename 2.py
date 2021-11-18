from selenium import webdriver
from ipr_sogaz.settings import *
from vk import *
import time
from selenium.webdriver.common.by import By

useragents={'ie':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            'chrome':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragents.get('chrome')}")
options.add_argument('--disable-blink-features=AutomationControlled')
# options.headless=True

driver = webdriver.Chrome(chromedriver, options=options)
driver.set_window_size(1920, 1080)
url = 'https://vk.com'


try:
    driver.get(url=url)
    time.sleep(3)
    driver.find_element(By.ID, 'index_email').send_keys(login)
    driver.find_element(By.ID, 'index_pass').send_keys(password)
    driver.find_element(By.ID, 'index_login_button').click()
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()