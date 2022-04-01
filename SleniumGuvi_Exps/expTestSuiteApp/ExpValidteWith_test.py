import pytest

@pytest.mark.ADS
def test_goToHomePage(test_getCookies_data):
    print("\nI am in home page!!",test_getCookies_data)

@pytest.mark.ADS
def test_app_NavigateToRecommendedProduct():
    print("\nclick on Trenddding Product!!!")


def test_NavigateToPDpage(test_getCookies_data):
    print("\nI am on Product details apge!!!",test_getCookies_data)