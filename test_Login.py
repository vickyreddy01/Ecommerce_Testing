import csv
import time

import pytest
from selenium.webdriver.common.by import By


# Utility function to load CSV data
def load_data(file_path):
    with open(file_path, mode='r') as file:
        return list(csv.DictReader(file))


@pytest.mark.usefixtures("setup")
class TestLoginPage:
    @pytest.mark.parametrize("data", load_data("../Data/Login_Data.csv"))
    def test_login_valid_credentials(self, data):
        # Retrieve the username and password from the CSV data
        username, password = data["username"], data["password"]

        # Perform login actions using the parameters
        self.driver.find_element(By.ID, "username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "signInBtn").click()

        time.sleep(5)
