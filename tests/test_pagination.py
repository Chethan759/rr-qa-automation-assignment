import pytest
from .pages.home_page import HomePage

@pytest.mark.regression
def test_next_prev_pagination(driver, base_url):
    hp = HomePage(driver, base_url)
    hp.open_home()
    cards = driver.find_elements(*hp.CARD)
    first_text = cards[0].text if cards else ""
    next_btns = driver.find_elements(*hp.PAGINATION_NEXT)
    if next_btns:
        next_btns[0].click()
        assert driver.find_elements(*hp.CARD), "Expected results after Next"
        new_cards = driver.find_elements(*hp.CARD)
        new_first = new_cards[0].text if new_cards else ""
        assert new_first != first_text, "Expected first card to change after Next"
    prev_btns = driver.find_elements(*hp.PAGINATION_PREV)
    if prev_btns:
        prev_btns[0].click()
        assert driver.find_elements(*hp.CARD), "Expected results after Previous"

@pytest.mark.negative
def test_last_page_edge_case(driver, base_url):
    hp = HomePage(driver, base_url)
    hp.open_home()
    last_btns = driver.find_elements(*hp.PAGINATION_LAST)
    if last_btns:
        last_btns[0].click()
        assert driver.title is not None
    else:
        pytest.skip("No explicit 'Last' page button available")
