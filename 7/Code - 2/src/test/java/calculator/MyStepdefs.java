package calculator;

import cucumber.api.PendingException;
import cucumber.api.java.Before;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.junit.Assert;

public class MyStepdefs {
    private Calculator calculator;
    private int value1;
    private int value2;

    private char opt;

    private int result;

    @Before
    public void before() {
        calculator = new Calculator();
    }

    @Given("^Two input values, (-?\\d+) and (-?\\d+)$")
    public void twoInputValuesAnd(int arg0, int arg1) {
        value1 = arg0;
        value2 = arg1;
    }

    @When("^I add the two values$")
    public void iAddTheTwoValues() {
        result = calculator.add(value1, value2);
    }

    @Then("^I expect the result (-?\\d+)$")
    public void iExpectTheResult(int arg0) {
        Assert.assertEquals(arg0, result);
    }

    @When("^I divide the two values$")
    public void iDivideTheTwoValues() {
        result = calculator.divide(value1, value2);
    }

    @When("^I power the two values$")
    public void iPowerTheTwoValues() {
        result = calculator.power(value1, value2);
    }

    @Given("^Three input values, (-?\\d+) and (-?\\d+) and ([/^])$")
    public void threeInputValuesAndAnd(int arg0, int arg1, char opt) {
        value1 = arg0;
        value2 = arg1;
        this.opt = opt;
    }

    @When("^I apply the operation to the two values$")
    public void iApplyTheOperationToTheTwoValues() {
        if (opt == '/') {
            result = calculator.divide(value1, value2);
        } else if (opt == '^') {
            result = calculator.power(value1, value2);
        } else {
            result = -1;
        }
    }

}