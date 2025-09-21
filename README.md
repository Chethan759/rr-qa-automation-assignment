# RR – QA Automation Assignment (Python Selenium + Pytest)
**Pinned for Python 3.12.x | Selenium 4.17.x | Pytest 8.1.1**

Demo under test: `https://tmdb-discover.surge.sh/`

## Quick Start (Windows CMD)
```bat
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -n auto --html=reports\report.html --self-contained-html
start "" reports\report.html
```

## Notes
- Selenium **4.17.12** is not available on PyPI. The closest stable is **4.17.2**, which is pinned here.
- Works with Chrome + webdriver-manager (downloads the matching driver automatically).
- Network/API assertions use `selenium-wire`.
