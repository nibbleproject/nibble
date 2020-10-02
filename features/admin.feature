Feature: Admin account
    As an admin
    I want to have access to an admin account
    so that I can manage the service.

    Scenario: logging in
        Given an admin user exists
        When I go to the path /accounts/login
        And I enter my username and password
        Then I should be logged in
