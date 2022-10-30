Feature: Sign up
  Background: Go to sign up page
    Given I am on the sign-up page

  Scenario Outline: Try sign up with wrong/valid format email
    When I click personal
    And I click continue
    And I enter "Adrian" in first name field
    And I click continue
    And I enter "Carpenter" in last name field
    And I click continue
    And I enter "<email>" in the email field
    Then A message with text "Please enter a valid email address." is <status>

  Examples: Try sign up with wrong/valid format email
    |email              |status       |
    |something@         |displayed    |
    |something@gmail.com|not displayed|


