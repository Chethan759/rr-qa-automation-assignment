import os
import pytest
from seleniumwire import webdriver  # type: ignore
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=None, help="Override BASE_URL")
    parser.addoption("--headed", action="store_true", help="Run headed (disable headless)")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    load_dotenv()
    return pytestconfig.getoption("--base-url") or os.getenv("BASE_URL", "https://tmdb-discover.surge.sh")

@pytest.fixture(scope="function")
def driver(pytestconfig):
    load_dotenv()
    headless_env = os.getenv("HEADLESS", "true").lower() == "true"
    headed_cli = pytestconfig.getoption("--headed")
    headless = headless_env and not headed_cli

    chrome_options = ChromeOptions()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1440,900")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    sw_options = {
        "verify_ssl": False,
        "enable_h2": True,
        "request_storage": "memory",
        "request_storage_max_size": 2000
    }

    drv = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options,
        seleniumwire_options=sw_options,
    )
    yield drv
    drv.quit()

def pytest_html_report_title(report):
    report.title = "RR – QA Automation Assignment (Selenium + Pytest)"
