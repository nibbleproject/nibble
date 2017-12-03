Feature: Admin account
    As an artist
    I want to have access to an admin account
    so that I can manage my comics.

    Scenario: logging in
        Given an admin user exists
        When I go to the admin page
        And I enter my username and password
        Then I should be logged in as an admin

    Scenario: email
        Given an admin user exists
        When I go to the admin page
        And I enter my username and password
        And I go to my user page
        Then I should see the email address I chose
