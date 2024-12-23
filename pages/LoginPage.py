from selenium.webdriver.common.by import By

class loginpage():
    def __init__(self, driver):
        self.driver = driver
        self.username_locator_name="username"
        self.password_locator_name="password"
        self.login_locator_xpath="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_locator_name).clear()
        self.driver.find_element(By.NAME, self.username_locator_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_locator_name).clear()
        self.driver.find_element(By.NAME, self.password_locator_name).send_keys(password)

    def click_login(self):
            self.driver.find_element(By.XPATH, self.login_locator_xpath).click()


