
from selenium import webdriver
from settings import *
import time
from selenium.webdriver.common.by import By


useragents={'ie':'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            'chrome':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument(f"user-agent={useragents.get('chrome')}")
chromeoptions.add_argument('--disable-blink-features=AutomationControlled')
# chromeoptions.headless=True

ffoptions = webdriver.FirefoxOptions()
# ffoptions.headless=True
ffoptions.add_argument('--disable-blink-features=AutomationControlled')

def driver(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=chromedriver, options=chromeoptions)
        return driver

    elif browser == 'ff':
        driver = webdriver.Firefox(executable_path=geckodriver, options=ffoptions)
        return driver



class Elements():
    def __init__(self, browser=None, **kwargs):
        self.driver=driver(browser)
        self.url = 'https://shop.sogaz.ru/'
        self.result=[]
        self.output = {}
        for key, value in kwargs.items():
            self.output.update(**{key: value})

    def __str__(self):
        Elements.calculate(self)
        return str(self.result)

    def calculate(self):
        try:
            result=[]
            self.driver.set_window_size(1920, 1080)
            self.driver.get(url=self.url)

            # time.sleep(1)
            self.driver.find_element(By.XPATH, "(//I[@class='icon-del'])[5]").click()
            elements = self.driver.find_elements(By.CLASS_NAME, 'service__card')
            for element in elements:
                el_text = element.text
                sub_el_text=[]
                sub_elements = element.find_elements(By.XPATH, "div[2]/a")
                for i in sub_elements:
                    sub_el_text.append(i.get_attribute('text'))
                z = str(Elements(**{el_text: sub_el_text}).output)
                result.append(z)
                # self.result.append(z)
            self.result = result
            # return (result)
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()

    def __eq__(self, other):
        if isinstance(other, Elements):
            if self.result == other.result:
                return 'разделы и их содержимое совпадают'
            else:
                return 'не удалось сравньть объекты'


a=Elements('chrome')
b=Elements('ff')

print(a)
print(b)
print(a==b)

# ВЫВОД
#["{'Автострахование': ['ОСАГОонлайн', 'Автокаскозаявка', 'АВТО-НСонлайн']}", "{'Недвижимость': ['Простое решение для квартирыонлайн', 'Оптимальное решение для квартирыонлайн', 'Оптимальное решение для дома', 'Страхование ипотекизаявка', 'Персональное решение для квартирызаявка', 'Персональное решение для домазаявка', 'Программа страхования жилья Москвы', 'Программа страхования жилья в Ленинградской области']}", "{'Путешествие': ['Путешествия за рубеж (за границу)онлайн', 'Путешествия по Россиионлайн']}", "{'Здоровье': ['Доктор Лайконлайн', 'ПЕРСОНА Экономонлайн', 'ПЕРСОНА Антиклещонлайн', 'ПЕРСОНА Специальныйонлайн', 'ПЕРСОНА Универсальныйзаявка', 'Онкопомощьонлайн', 'Спроси врачаонлайн', 'Страхование пассажиров']}", "{'Жизнь и накопления': ['Копилка', 'Уверенный старт', 'Мультизащита', 'Индекс доверия']}"]
# ["{'Автострахование': ['ОСАГОонлайн', 'Автокаскозаявка', 'АВТО-НСонлайн']}", "{'Недвижимость': ['Простое решение для квартирыонлайн', 'Оптимальное решение для квартирыонлайн', 'Оптимальное решение для дома', 'Страхование ипотекизаявка', 'Персональное решение для квартирызаявка', 'Персональное решение для домазаявка', 'Программа страхования жилья Москвы', 'Программа страхования жилья в Ленинградской области']}", "{'Путешествие': ['Путешествия за рубеж (за границу)онлайн', 'Путешествия по Россиионлайн']}", "{'Здоровье': ['Доктор Лайконлайн', 'ПЕРСОНА Экономонлайн', 'ПЕРСОНА Антиклещонлайн', 'ПЕРСОНА Специальныйонлайн', 'ПЕРСОНА Универсальныйзаявка', 'Онкопомощьонлайн', 'Спроси врачаонлайн', 'Страхование пассажиров']}", "{'Жизнь и накопления': ['Копилка', 'Уверенный старт', 'Мультизащита', 'Индекс доверия']}"]
# разделы и их содержимое совпадают

