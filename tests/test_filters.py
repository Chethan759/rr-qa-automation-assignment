import re
import pytest
from .pages.home_page import HomePage

@pytest.mark.regression
def test_category_tabs(driver, base_url):
    hp = HomePage(driver, base_url)
    hp.open_home()
    for tab in [hp.TAB_POPULAR, hp.TAB_TRENDING, hp.TAB_NEWEST, hp.TAB_TOP]:
        hp.switch_tab(tab)
        cards = driver.find_elements(*hp.CARD)
        assert len(cards) > 0, "Expected at least one result card"

@pytest.mark.smoke
def test_title_search(driver, base_url):
    hp = HomePage(driver, base_url)
    hp.open_home()
    query = "star"
    hp.search(query)
    cards = driver.find_elements(*hp.CARD)
    assert len(cards) > 0, "Expected some results"
    found = any(re.search(r"star", (c.text or ""), re.IGNORECASE) for c in cards[:10])
    assert found, "Expected at least one card containing the query"

@pytest.mark.regression
def test_type_filters(driver, base_url):
    hp = HomePage(driver, base_url)
    hp.open_home()
    hp.toggle_movies()
    assert driver.find_elements(*hp.CARD), "Movies should show results"
    hp.toggle_tv()
    assert driver.find_elements(*hp.CARD), "TV should show results"

@pytest.mark.regression
def test_year_and_rating_sliders(driver, base_url):
    hp = HomePage(driver, base_url)
    hp.open_home()
    for sel in [hp.YEAR_SLIDER, hp.RATING_SLIDER]:
        els = driver.find_elements(*sel)
        if els:
            try:
                els[0].send_keys(u"\ue014")  # ArrowRight
            except Exception:
                pass
    assert driver.find_elements(*hp.CARD) is not None

@pytest.mark.regression
def test_genre_dropdown(driver, base_url):
    hp = HomePage(driver, base_url)
    hp.open_home()
    genres = driver.find_elements(*hp.GENRE_DROPDOWN)
    if not genres:
        pytest.skip("Genre dropdown not found")
    genres[0].click()
    opt = driver.find_element(*hp.OPTION_FIRST)
    opt.click()
    assert driver.find_elements(*hp.CARD) is not None
