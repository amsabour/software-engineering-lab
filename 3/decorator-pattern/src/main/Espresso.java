package main;

public class Espresso implements Beverage{
    @Override
    public String getDescription() {
        return "Delicious Espresso";
    }

    @Override
    public double cost() {
        return 1.99;
    }
}
