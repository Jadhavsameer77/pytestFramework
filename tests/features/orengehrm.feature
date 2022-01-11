Feature: OrangeHRM login

  Scenario: As a client I want to Login into OrangeHRM
    Given launch chrome browser
    When Open orangeHRM login page
    And Enter username and password
    Then Login get successfully
    And Close the browser