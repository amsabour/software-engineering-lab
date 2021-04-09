package main;

public abstract class CondimentDecorator implements Beverage {
    private Beverage _beverage;

    public CondimentDecorator(Beverage _beverage) {
        this._beverage = _beverage;
    }

    public Beverage getBeverage() {
        return _beverage;
    }

    @Override
    public String getDescription() {
        return getBeverage().getDescription();
    }

    @Override
    public double cost() {
        return getBeverage().cost();
    }
}
