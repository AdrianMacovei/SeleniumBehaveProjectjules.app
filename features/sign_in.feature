Feature: Sign in
  Background: Sign in page start
    Given I am on the sign-in page

  Scenario: Sign up link redirect to sign up page
    When I click the sign-up link
    Then I am redirected to the sign-up page

  Scenario Outline: Try to sign in with invalid email format and invalid password
    When I enter "<email>" in email field
    And I enter "<password>" in password field
    Then Login button should not be enable
    And A red message with text "Please enter a valid email address!" appears

  Examples: Sign in invalid credentials
    |email              |password              |
    |something@gmail.   |7-8Characters         |
    |morning@           |7-8Characters         |
    |something@gmail    |A123456789!           |
    |something@gmail1234|password1234!         |

  Scenario: Enter password and delete it give warning message
    When I enter "adrianmacovei17@gmail.com" in email field
    And I enter "SuperSecretPassword26!" in password field
    And I delete the password
    Then Login button should not be enable
    And A red message with text "Please enter your password!" appears

  Scenario Outline: Sign in with valid email format and invalid passwords flash message
    When I enter "<email>" in email field
    And I enter "<password>" in password field
    And I click login button
    Then A flash message with text "Invalid email/password combination" appears

   Examples: Sign in with valid email format and invalid passwords
    |email                      |password              |
    |something@gmail.com        |7-8Characters         |
    |morning@yahoo.com          |7-8Characters         |
    |adrianmamcovei17@gmail.com |A123456789!           |
    |citron@hotmail.com         |password1234!         |

  Scenario: Forgot password link redirect to forgot password page
    When I click the forgot password link
    Then I am redirected to the forgot password page


  Scenario: Sign in with valid credentials
    When I enter "adrianmacovei17@gmail.com" in email field
    And I enter "SuperSecretPassword26!" in password field
    And I click login button
    Then I am redirected to the search all page
    And The page title will be "Search"