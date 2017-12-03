Feature: Smoke tests
    As an admin
    I want the application to be running correctly
    so people can use it.

    Scenario: homepage
        When I visit the homepage
        Then the page should load
