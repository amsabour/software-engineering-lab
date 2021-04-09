package main;

public class Decaf implements Beverage {
    @Override
    public String getDescription() {
        return "Delicious Decaf";
    }

    @Override
    public double cost() {
        return 1.05;
    }
}
