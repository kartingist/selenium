from selenium import webdriver
from settings import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


useragents={'ie':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            'chrome':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragents.get('chrome')}")
options.add_argument('--disable-blink-features=AutomationControlled')
options.headless=True

driver = webdriver.Chrome(chromedriver, options=options)
driver.set_window_size(1920, 1080)
n=1
url = f'https://www.avito.ru/krasnodar?f=ASgCAgECAUXGmgwUeyJmcm9tIjoyMDAwLCJ0byI6MH0&p={n}&q=xiaomi+mi+%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA'
driver.implicitly_wait(10)

try:
    driver.get(url=url)
    pages_count = int(driver.find_elements(By.CLASS_NAME, 'pagination-item-JJq_j')[-2].text)
    this_page = int(driver.find_element(By.CLASS_NAME, 'pagination-item_active-NcJX6').text)
    next_page_button = driver.find_elements(By.CLASS_NAME, 'pagination-item_arrow-Sttbt')[1]
    file = open('test.txt', 'w')
    print(f'По результатам поиска найдено страниц: {pages_count}')
    while n <= pages_count:
        items = driver.find_elements(By.CLASS_NAME, 'iva-item-titleStep-_CxvN')
        q = 1
        for item in items:

            item.click()
            time.sleep(1)
            driver.switch_to.window(driver.window_handles[1])

            username = driver.find_element(By.CLASS_NAME, 'seller-info-name').text
            title = driver.find_element(By.CLASS_NAME, 'title-info-title-text').text
            price = driver.find_element(By.CLASS_NAME, 'js-item-price').get_attribute('content')
            link = driver.current_url
            file.write(f'{q}) {"*" * 30}\n')
            file.write(f"Продавец: {username}\nЗаголовок:{title}\nЦена:{price}\nСсылка:{link}\n")

            print(f"{q}) Продавец: {username}\nЗаголовок: {title}\nЦена: {price}\nСсылка: {link}\n", end='\n\n')
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            q+=1
        # q=1
        n += 1
        url = f'https://www.avito.ru/krasnodar/noutbuki?p={n}&q=xiaomi+mi+notebook+pro'
        driver.get(url=url)
        print(f"{'*'*30}\nПереход на страницу {n}\n{'*'*30}\n")
    file.close()
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


