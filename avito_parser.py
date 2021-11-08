from selenium import webdriver
from settings import *
import time
from selenium.webdriver.common.by import By

useragents={'ie':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            'chrome':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragents.get('chrome')}")
options.add_argument('--disable-blink-features=AutomationControlled')
options.headless=True

driver = webdriver.Chrome(chromedriver, options=options)
driver.set_window_size(1920, 1080)
url = 'https://www.avito.ru/krasnodar/noutbuki?q=xiaomi+mi+notebook+pro'


try:
    driver.get(url=url)
    driver.implicitly_wait(5)
    items = driver.find_elements(By.XPATH, '//div[@data-marker="item-photo"]')
    pages_count = int(driver.find_elements(By.CLASS_NAME, 'pagination-item-JJq_j')[-2].text)
    for item in items:
        item.click()
        driver.implicitly_wait(5)
        driver.switch_to.window(driver.window_handles[1])

        username = driver.find_element(By.CLASS_NAME,'seller-info-name').text
        title = driver.find_element(By.CLASS_NAME, 'title-info-title-text').text
        price = driver.find_element(By.CLASS_NAME, 'js-item-price').get_attribute('content')
        link = driver.current_url

        # file = open('test.txt', 'w')
        # file.write(username, )
        # file.close()
        print(f"Продавец: {username}\nЗаголовок:{title}\nЦена:{price}\nСсылка:{link}\n", end='\n')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


