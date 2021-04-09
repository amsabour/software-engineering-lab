package main;

public class DarkRoast implements Beverage {
    @Override
    public String getDescription() {
        return "Delicious DarkRoast";
    }

    @Override
    public double cost() {
        return 0.99;
    }
}
