from time import sleep

from PreimierLeague.pages.cookiesAndAdds import cookiesAndAdds
from PreimierLeague.pages.get_players_stats import get_player_stats
from PreimierLeague.tests.globals import url_base
from PreimierLeague.tests.seleniumBaseFile import seleniumBaseFile


class testPlayersStats():
    base = seleniumBaseFile()

    driver = base.selenium__start(url_base)
    cookies_And_Adds = cookiesAndAdds(driver)
    player_stats = get_player_stats(driver)

    cookies_And_Adds.accept_all_cookies()
    cookies_And_Adds.close_ad()
    player_stats.player_page()
    player_stats.search_player_name()
    player_stats.click_player()
    sleep(3)
    player_stats.click_stats()
    sleep(3)
    player_stats.player_record()
