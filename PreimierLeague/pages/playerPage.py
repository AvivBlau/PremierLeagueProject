from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class playerPage():

    def __init__(self, driver):
        self.driver = driver
        self.search_player_name_locator = "input[id='search-input']"
        self.player_page_locator = "Players"
        self.click_player_locator = "player__name"
        self.click_stats_locator = "A[data-text='Stats']"
        self.goals_locator = "span[data-stat='goals']"
        self.assists_locator = "span[data-stat='goal_assist']"
        self.appearances_locator = "span[data-stat='appearances']"

    def players_page(self):
        players_page = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.player_page_locator)
        players_page.click()

    def search_player_name(self, player_name):
        search_player = self.driver.find_element(By.CSS_SELECTOR, self.search_player_name_locator)
        search_player.click()
        search_player.clear()
        search_player.send_keys(player_name)
        search_player.send_keys(Keys.ENTER)

    def click_player_and_stats(self):
        click_player_stats = self.driver.find_element(By.CLASS_NAME, self.click_player_locator)
        click_player_stats.click()
        click_player_stats = self.driver.find_element(By.CSS_SELECTOR, self.click_stats_locator)
        click_player_stats.click()

    def get_player_stats(self, player):
        goals = self.driver.find_element(By.CSS_SELECTOR, self.goals_locator).text
        assists = self.driver.find_element(By.CSS_SELECTOR, self.assists_locator).text
        appearances = self.driver.find_element(By.CSS_SELECTOR, self.appearances_locator).text
        print(f"The number of {player} goals is : {goals} ")
        print(f"The number of {player} assists is : {assists} ")
        print(f"The number of {player} appearances is : {appearances} ")
        goals_as_int = int(goals)
        assists_as_int = int(assists)
        appearances_as_int = int(appearances)
        assert goals_as_int > 200, "Something went wrong the number of goals decreased"
        assert assists_as_int > 45, "Something went wrong the number of assists decreased"
        assert appearances_as_int > 300, "Something went wrong the number of appearances decreased"
        goal_contributions = (goals_as_int + assists_as_int) / appearances_as_int
        print(f"The number of {player} goalcontributions is per game : {goal_contributions} ")
        return goal_contributions
