Feature: Dashboard
    As an artist
    I want to have access to a dashboard
    so that I can manage my comics.

    Scenario: logging in
        Given a regular user exists
        When I go to the path /accounts/login/
        And I enter my username and password
        Then I should be taken to /dashboard/
