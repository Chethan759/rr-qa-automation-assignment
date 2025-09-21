import pytest

@pytest.mark.api
def test_discovery_api_calls_ok(driver, base_url):
    driver.scopes = ['.*']
    driver.request_interceptor = None
    driver.response_interceptor = None

    driver.get(base_url)

    api_reqs = [r for r in driver.requests if r.response and ('api' in r.url or 'discover' in r.url)]
    assert len(api_reqs) > 0, "Expected at least one API discovery/search call"

    not_ok = [r for r in api_reqs if r.response is None or r.response.status_code >= 400]
    assert not not_ok, f"Some API calls failed: {[ (r.url, getattr(r.response,'status_code',None)) for r in not_ok ]}"

    json_like = sum(1 for r in api_reqs if 'application/json' in (r.response.headers.get('Content-Type', '')).lower())
    assert json_like > 0, "Expected JSON responses among discovery calls"
