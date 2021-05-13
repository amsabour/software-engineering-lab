@tag
Feature: Power

  Scenario: power two numbers
    Given Two input values, 50 and 3
    When I power the two values
    Then I expect the result 125000


  Scenario Outline: power two numbers -- powering is valid
    Given Two input values, <first> and <second>
    When I power the two values
    Then I expect the result <result>
    Examples:
      | first | second | result |
      | 6     | 3      | 216    |
      | 10    | 2      | 100    |
      | 35    | 3      | 42875  |

  Scenario Outline: power two numbers -- powering is invalid
    Given Two input values, <first> and <second>
    When I power the two values
    Then I expect the result <result>
    Examples:
      | first | second | result |
      | 6     | -1     | -1     |
      | 10    | -2     | -1     |
      | 35    | -10    | -1     |
