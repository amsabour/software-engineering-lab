package main;

public class SteamedMilk extends CondimentDecorator {
    public SteamedMilk(Beverage _beverage) {
        super(_beverage);
    }

    @Override
    public double cost() {
        return 0.10 + super.cost();
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " with milk";
    }
}
