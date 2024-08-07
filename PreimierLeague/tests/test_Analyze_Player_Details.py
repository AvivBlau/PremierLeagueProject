import unittest
from PreimierLeague.pages.cookiesAndAdds import cookiesAndAdds
from PreimierLeague.pages.playerPage import playerPage
from PreimierLeague.tests.globals import url_base, player1, player2
from PreimierLeague.tests.seleniumBaseFile import seleniumBaseFile


class test_Analyze_Player_Details(unittest.TestCase):

    def setUp(self):
        base = seleniumBaseFile()
        self.driver = base.selenium__start(url_base)
        self.base = base

    def test_Analyze_Player_Details(self):
        cookies_And_Adds = cookiesAndAdds(self.driver)
        player_stats = playerPage(self.driver)

        cookies_And_Adds.accept_all_cookies()
        cookies_And_Adds.close_ad()
        player_stats.players_page()
        player_stats.search_player_name(player1)
        player_stats.click_player_stats()
        player_stats.get_player_stats(player1)
        player_stats.players_page()
        player_stats.search_player_name(player2)
        player_stats.click_player_stats()
        player_stats.get_player_stats(player2)

    def tearDown(self):
        self.base.selenium__end(self.driver)
