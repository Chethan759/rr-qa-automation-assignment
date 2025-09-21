from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    TAB_POPULAR = (By.XPATH, "//*[@role='link' and normalize-space()='Popular'] | //a[normalize-space()='Popular']")
    TAB_TRENDING = (By.XPATH, "//*[@role='link' and normalize-space()='Trending'] | //a[normalize-space()='Trending']")
    TAB_NEWEST = (By.XPATH, "//*[@role='link' and normalize-space()='Newest'] | //a[normalize-space()='Newest']")
    TAB_TOP = (By.XPATH, "//*[@role='link' and normalize-space()='Top Rated'] | //a[normalize-space()='Top Rated']")

    TYPE_MOVIES = (By.XPATH, "//*[@role='button' and contains(., 'Movies')] | //button[contains(., 'Movies')]")
    TYPE_TV = (By.XPATH, "//*[@role='button' and contains(., 'TV')] | //button[contains(., 'TV')]")

    SEARCH = (By.XPATH, "//input[contains(@placeholder,'Search') or @type='search']")
    CARD = (By.CSS_SELECTOR, "[data-testid='title-card'], .card, [class*='card']")

    YEAR_SLIDER = (By.CSS_SELECTOR, "[data-testid='year-slider'], [aria-label*='Year']")
    RATING_SLIDER = (By.CSS_SELECTOR, "[data-testid='rating-slider'], [aria-label*='Rating']")
    GENRE_DROPDOWN = (By.CSS_SELECTOR, "[data-testid='genre-select'], [aria-haspopup='listbox']")
    OPTION_FIRST = (By.XPATH, "//*[@role='option'][1]")

    PAGINATION_NEXT = (By.XPATH, "//*[@role='button' and normalize-space()='Next'] | //button[normalize-space()='Next']")
    PAGINATION_PREV = (By.XPATH, "//*[@role='button' and normalize-space()='Previous'] | //button[normalize-space()='Previous']")
    PAGINATION_LAST = (By.XPATH, "//*[@aria-label='Last page'] | //*[@role='button' and (normalize-space()='Last' or @aria-label='Last page')]")

    def open_home(self):
        self.open("/")

    def switch_tab(self, tab_locator):
        self.click(tab_locator)

    def search(self, text: str):
        el = self.type(self.SEARCH, text)
        el.submit()

    def toggle_movies(self):
        try:
            self.click(self.TYPE_MOVIES)
        except Exception:
            pass

    def toggle_tv(self):
        try:
            self.click(self.TYPE_TV)
        except Exception:
            pass
