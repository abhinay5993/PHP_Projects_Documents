import pytest
import os

@pytest.mark.ADS
def test_app_launchBrowser(test_getCookies_data):
    print("\nLaunch Borwser app!!...")
    print("\nLauching my scripts into : ",os.times())

def test_logIntoGmail():
    print("\nEnter UserName : ")
    print("\nEnter Password : ")
    assert True==True

def test_app_pressSubmitToLoginButtion():
    print("\nclick on LogIn button!!!..")
    assert 10==10

@pytest.mark.parametrize("num,output",[(1,10),(2,20),(3,30),(4,40),(5,52)])
def test_mutiplyWithTestData(num,output):
    assert num*10==output

