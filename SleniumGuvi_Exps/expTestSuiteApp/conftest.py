import pytest

@pytest.fixture
def test_getCookies_data():
    x_xsrf_token="abhiany@jhffh448@^&#^#&^&@^&^##"
    hoz_jwt="kkatif__@)_)))E)_"
    print("\nget Tokens to Authenticate!!!..")
    return hoz_jwt,x_xsrf_token