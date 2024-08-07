from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

class seleniumBaseFile():
    def selenium__start(self, url):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def selenium__end(self, driver):
        driver.close()
        print("test end")