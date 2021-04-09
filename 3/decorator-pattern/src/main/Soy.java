package main;

public class Soy extends CondimentDecorator {
    public Soy(Beverage _beverage) {
        super(_beverage);
    }

    @Override
    public double cost() {
        return 0.15 + super.cost();
    }

    @Override
    public String getDescription() {
        return super.getDescription() + " with soy";
    }
}
