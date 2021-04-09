package main;

public class SimplePower implements PowerOperation {
    private MultiplicationOperation multOp;

    public SimplePower(MultiplicationOperation multOp) {
        this.multOp = multOp;
    }

    public void SetMultOp(MultiplicationOperation multOp) {
        this.multOp = multOp;
    }

    @Override
    public int Apply(int a, int b) {
        return 0;
    }
}
