from selenium.webdriver.common.by import By

class homepage():
    def __init__(self, driver):
        self.driver = driver
        self.userdropdown_locator_Xpath="/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span"
        self.logout_locator_linktext="Logout"

    def click_userdropdown(self):
            self.driver.find_element(By.XPATH, self.userdropdown_locator_Xpath).click()



    def click_logout(self):
            self.driver.find_element(By.LINK_TEXT, self.logout_locator_linktext).click()