package main;

public class Mocha extends CondimentDecorator {
    public Mocha(Beverage _beverage) {
        super(_beverage);
    }

    @Override
    public double cost() {
        return 0.20 + super.cost();
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " with mocha";
    }
}

