Feature: Multiple domains
    As an admin
    I want to use multiple domains
    so that I can host multiple comics.

    Scenario: different domains
        When I go to the site on a different domain
        Then the request should succeed
