import time

import allure
import pytest

from conftest import test_setup
from pages.LoginPage import loginpage
from pages.HomePage import homepage
from utils import utils as utils
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():
    # @pytest.fixture(scope="class")
    # #we use fixture so that the function which we want to run once and the function which we want to close at one. We use scope as session
    # #because after login i dot want to close the browser and then start it agsin so i use scope.
    # def test_setup(self):
    #     global driver
    #     driver=webdriver.Firefox()
    #     driver.implicitly_wait(5)
    #     driver.maximize_window()
    #     yield
    #     driver.close()

    def test_login(self):
        driver=self.driver
        driver.get(utils.URL)
        login = loginpage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()


    def test_logout(self):
        try:
         driver=self.driver
         home=homepage(driver)
         home.click_userdropdown()
         home.click_logout()
         title=driver.title
         assert title==("abc")


        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            time.sleep(2)
            testName=utils.whoami()
            currTime=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshotName= testName+"_"+ currTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName, attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/aprab/PycharmProjects/Automation Framework/screebshots/"+ screenshotName+".png")
            raise

        except:
            print("There is exception")
            raise

        else:
            print("No exceptions occurred")


        finally:
            print("I am inside finally block")





