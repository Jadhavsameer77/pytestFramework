import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_bdd import *
from selenium import webdriver
from PageObjects import OHRMPage

userid= OHRMPage.orangeHRM.username
pwd=OHRMPage.orangeHRM.pwd
loginBtn=OHRMPage.orangeHRM.loginBtn
url=OHRMPage.orangeHRM.url

scenarios('../features/orengehrm.feature')

@allure.severity(allure.severity_level.NORMAL)
@pytest.fixture
def browser():
    b = webdriver.Chrome
    #b.implicitly_wait(10)
    yield b
    pass

@given('launch chrome browser')
def launchBrowser(browser):
   browser.driver=webdriver.Chrome()
   browser.driver.maximize_window()

@when('Open orangeHRM login page')
def launchOHRMP(browser):
    browser.driver.get(url)
    allure.attach(browser.driver.get_screenshot_as_png(), name="OrangeHRMLogin", attachment_type=AttachmentType.PNG)

@when('Enter username and password')
def creds(browser):
    browser.driver.find_element_by_css_selector(userid).send_keys("Admin")
    browser.driver.find_element_by_css_selector(pwd).send_keys("admin123")
    allure.attach(browser.driver.get_screenshot_as_png(), name="OrangeHRMLogin", attachment_type=AttachmentType.PNG)

@then(u'Login get successfully')
def loginSuccess(browser):
    browser.driver.find_element_by_css_selector(loginBtn).click()
    temp=browser.driver.find_element_by_css_selector("[id='welcome']").text
    assert "Welcome1" in temp,allure.attach(browser.driver.get_screenshot_as_png(),
    name="OrangeHRMLogin", attachment_type=AttachmentType.PNG)
    allure.attach(browser.driver.get_screenshot_as_png(), name="OrangeHRMLogin", attachment_type=AttachmentType.PNG)

@then('Close the browser')
def tearDown(browser):
    browser.driver.close()
