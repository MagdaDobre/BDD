Feature: Check the Sign_In functionality in Jules App

  Background:
    Given signin: I am a user on Jules sign-in page

  @test1
  Scenario: Check error message when password is empty and login button is disabled
    When signin: I fill in the email "test1@microsoft.com"
    When signin: i leave empty the password field
    When signin: I check the password error message ‘Please enter your password!’ is displayed
    Then signin: I check the button login is disabled