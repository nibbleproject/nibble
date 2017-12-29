Feature: Creating an account
    As an author
    I want to create an account
    so I can post comics.

    Scenario: sign up
        When I go to the home page
        And I click the "Sign Up" link
        And I fill out the sign up form
        And I click the "Continue" button
        Then a new user should be created
        And a confirmation email should be sent
        And I should see the email confirmation notice

     Scenario: signing up without an email
        When I go to the home page
        And I click the "Sign Up" link
        And I fill out the sign up form without an email
        And I click the "Continue" button
        Then no new user should be created

     Scenario: logging in with an unconfirmed account
        Given an unconfirmed account
        When I log in
        Then I should see the email confirmation notice

     Scenario: confirming an email
        Given an unconfirmed account
        When I go to the email confirmation URL
        And I click the "Confirm" button
        Then my email should be confirmed
        And I should be taken to the dashboard
        And I should see a message saying "confirmed"

     Scenario: logging in with a confirmed account
        Given a confirmed account
        When I log in
        Then I should be taken to the dashboard
