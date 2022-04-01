import pytest

@pytest.fixture
def test_getApp_url():
    url='https://www.youtube.com/'
    print("\nLaunch The URl - ",url)
    return url

@pytest.fixture
def test_app_logIn(test_getCookies_data):
    print("\nReceived Data : ",test_getApp_url)
    email="testApp@caratlane.com"
    pss="*&&$*&$*$"
    print("\nperform login useing : - email - ",email,"pass : ",pss)
    return email,pss


def test_get_PD_page(test_getApp_url,test_app_logIn):
    print("\nget prouct Details : ",test_getApp_url)
    for i in range(0,9):
        print("\nGet Iter value : ",test_app_logIn)