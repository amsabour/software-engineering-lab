package main;

public class HouseBlend implements Beverage {
    @Override
    public String getDescription() {
        return "Delicious HouseBlend";
    }

    @Override
    public double cost() {
        return 0.89;
    }
}
