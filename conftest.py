import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
    #we use fixture so that the function which we want to run once and the function which we want to close at one. We use sco[e as session
    #because after login i dot want to close the browser and then start it agsin so i use scope.
#def test_setup(self):
def test_setup(request):
    #global driver
    driver=webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()