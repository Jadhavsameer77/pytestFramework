import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_bdd import *
from selenium import webdriver

from PageObjects import timetrackerPage

scenarios('../features/timetracker.feature')

url=timetrackerPage.timeT.url
username=timetrackerPage.timeT.uName
email=timetrackerPage.timeT.email
pwd=timetrackerPage.timeT.pwd
submit=timetrackerPage.timeT.submit

@allure.severity(allure.severity_level.BLOCKER)
@pytest.fixture
def browser():
    b = webdriver.Chrome
    #b.implicitly_wait(10)
    yield b
    pass


@given('I launch chrome browser')
def launchBrowser(browser):
   browser.driver=webdriver.Chrome()
   browser.driver.maximize_window()



@when('Open timetracker login page')
def launchOHRMP(browser):
    browser.driver.get(url)
    title = browser.driver.title
    assert "Registration" in title,allure.attach(browser.driver.get_screenshot_as_png(),
    name="OrangeHRMLogin", attachment_type=AttachmentType.PNG)
    allure.attach(browser.driver.get_screenshot_as_png(), name="OrangeHRMLogin", attachment_type=AttachmentType.PNG)


@when('I Enter credentials')
def creds(browser):
    browser.driver.find_element_by_css_selector(username).send_keys("abcd")
    browser.driver.find_element_by_css_selector(email).send_keys("abcd123@gmail.com")
    browser.driver.find_element_by_css_selector(pwd).send_keys("admin123")
    allure.attach(browser.driver.get_screenshot_as_png(), name="OrangeHRMLogin", attachment_type=AttachmentType.PNG)



@then('Registration in timetracker get successfully')
def loginSuccess(browser):
    browser.driver.find_element_by_css_selector(submit).click()
    allure.attach(browser.driver.get_screenshot_as_png(), name="OrangeHRMLogin", attachment_type=AttachmentType.PNG)


@then('I Close the browser')
def tearDown(browser):
    browser.driver.close()
