@tag
Feature: All Operations

  Scenario: operate two numbers -- divide
    Given Three input values, 50 and 3 and /
    When I apply the operation to the two values
    Then I expect the result 16

  Scenario: operate two numbers -- power
    Given Three input values, 16 and 5 and ^
    When I apply the operation to the two values
    Then I expect the result 1048576

  Scenario Outline: operate two numbers -- everything
    Given Three input values, <first> and <second> and <opt>
    When I apply the operation to the two values
    Then I expect the result <result>
    Examples:
      | first | second | opt | result |
      | 6     | 2      | /   | 3      |
      | 6     | 2      | ^   | 36     |
      | 10    | 3      | ^   | 1000   |
      | 121   | 11     | /   | 11     |
      | 121   | -2     | ^   | -1     |


