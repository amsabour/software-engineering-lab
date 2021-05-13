@tag
Feature: Dividing
  Scenario: divide two numbers
    Given Two input values, 50 and 3
    When I divide the two values
    Then I expect the result 16


  Scenario Outline: divide two numbers -- dividing is valid
    Given Two input values, <first> and <second>
    When I divide the two values
    Then I expect the result <result>
    Examples:
      | first | second | result |
      | 6     | 3      | 2      |
      | 10    | 2      | 5      |
      | 35    | 7      | 5      |
