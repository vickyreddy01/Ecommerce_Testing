import requests
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
import csv

@pytest.fixture(scope='class')
def setup(request):
    chrome_option = Options()
    chrome_option.add_argument("--Maximized_window")
    #chrome_option.add_argument("--Headless")
    driver= webdriver.Chrome(options = chrome_option)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    request.cls.driver =driver

    yield
    driver.close()



