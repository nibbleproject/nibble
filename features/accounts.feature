Feature: Creating an account
    As an author
    I want to create an account
    so I can post comics.

    Scenario: signing up
        When I go to the home page
        And I click the "Sign Up" link
        And I fill out the sign up form
        And I click the "Continue" button
        Then a new user should be created
        And a confirmation email should be sent
        And I should be taken to /dashboard/

     Scenario: signing up without an email
        When I go to the home page
        And I click the "Sign Up" link
        And I fill out the sign up form without an email
        And I click the "Continue" button
        Then no new user should be created

     Scenario: confirming an email
        Given an unconfirmed account
        When I go to the email confirmation URL
        And I click the "Confirm" button
        Then my email should be confirmed
        And I should be taken to /accounts/login/
        And I should see a message saying "confirmed"

     Scenario: logging in
        Given a confirmed account
        When I log in
        Then I should be taken to /dashboard/
