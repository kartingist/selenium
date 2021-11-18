import random

from selenium import webdriver
from ipr_sogaz.settings import *
from selenium.webdriver.common.by import By

useragents={'ie':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            'chrome':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragents.get('chrome')}")
options.add_argument('--disable-blink-features=AutomationControlled')
# options.headless=True

driver = webdriver.Chrome(chromedriver, options=options)
driver.set_window_size(1920, 1080)
url='https://www.sogaz-med.ru/erh45h4rt5GEgr455/'
f=open('snils.txt', 'r')
lines=f.readlines()
try:
    for line in lines:
        snils = line.strip()
        print(snils)
        driver.get(url=url)
        driver.find_elements(By.ID, 'region-result-list')[0].find_element(By.XPATH, '//*[@id="region-result-list"]/option[31]').click()
        driver.find_elements(By.ID, 'point-result-list')[0].find_element(By.XPATH, '//*[@id="point-result-list"]/option[2]').click()
        driver.find_element(By.NAME, 'surname').send_keys('Тест')
        driver.find_element(By.NAME, 'name').send_keys('Тест')
        driver.find_element(By.NAME, 'second').send_keys('Тест')
        driver.find_element(By.NAME, 'date').send_keys('03081994')
        driver.find_element(By.NAME, 'snils').send_keys(snils)

        driver.find_element(By.NAME, 'phone').send_keys(random.randint(1000000000, 9999999999))
        driver.find_element(By.NAME, 'email').send_keys('awjon94@gmail.com')

        input()
        # driver.find_element(By.CLASS_NAME, 'feedback__form-agree feedback__form-agree--request').click()
        # time.sleep(25)

except Exception as ex:
    print(ex)
finally:
    # pass
    driver.close()
    driver.quit()





