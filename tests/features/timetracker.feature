Feature: Timetracker login process

  Scenario: As a client I want to Login into Timetracker
    Given I launch chrome browser
    When Open timetracker login page
    And I Enter credentials
    Then Registration in timetracker get successfully
    And I Close the browser