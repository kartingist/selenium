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
url = 'https://shop.sogaz.ru/'

class Elements:
    def __init__(self, **kwargs):
        self.output = {}
        for key,value in kwargs.items():
            self.output.update(**{key:value})




def main():
    result=[]
    try:
        driver.get(url=url)
        # time.sleep(1)
        driver.find_element(By.XPATH, "(//I[@class='icon-del'])[5]").click()
        elements = driver.find_elements(By.CLASS_NAME, 'service__card')
        for element in elements:
            el_text = element.text
            sub_el_text=[]
            sub_elements = element.find_elements(By.XPATH, "div[2]/a")
            for i in sub_elements:
                sub_el_text.append(i.get_attribute('text'))
            z=str(Elements(**{el_text: sub_el_text}).output)
            result.append(z)
        return (result)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

print(main())