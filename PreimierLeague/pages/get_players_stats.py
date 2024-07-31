import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class get_player_stats(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver


    def player_page(self):
        player_page = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Players")
        player_page.click()

    def search_player_name(self):
        search_harry_kane = self.driver.find_element(By.CSS_SELECTOR, "input[id='search-input']")
        search_harry_kane.click()
        search_harry_kane.clear()
        search_harry_kane.send_keys("Harry Kane")
        search_harry_kane.send_keys(Keys.ENTER)

    def click_player(self):
        click_player = self.driver.find_element(By.CSS_SELECTOR, "img[class='img player__name-image']")
        click_player.click()

    def click_stats(self):
        click_player = self.driver.find_element(By.CSS_SELECTOR, "A[data-text='Stats']")
        click_player.click()

    def player_record(self):
        goals = self.driver.find_element(By.CSS_SELECTOR, "span[data-stat='goals']").text
        assists = self.driver.find_element(By.CSS_SELECTOR, "span[data-stat='goal_assist']").text
        appearances = self.driver.find_element(By.CSS_SELECTOR, "span[data-stat='appearances']").text
        print(f"The number of Harry Kane goals is : {goals} ")
        print(f"The number of Harry Kane assists is : {assists} ")
        print(f"The number of Harry Kane appearances is : {appearances} ")
        assert goals == "213", "The number of goals is not 213"
        assert assists == "46", "The number of assists is not 46"
        assert appearances == "320", "The number of appearances is not 320"

        return int(goals), int(assists), int(appearances)
