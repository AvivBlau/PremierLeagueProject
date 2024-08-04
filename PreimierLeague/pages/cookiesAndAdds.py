from selenium.webdriver.common.by import By


class cookiesAndAdds():
    def __init__(self, driver):
        self.driver = driver

    def accept_all_cookies(self):
        cookies_button = self.driver.find_element(By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']")
        cookies_button.click()

    def close_ad(self):
        try:
            ad_button = self.driver.find_element(By.CLASS_NAME, "closeBtn")
            ad_button.click()
        except:
            print("No ad to close.")
