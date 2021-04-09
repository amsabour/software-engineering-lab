package main;

public class RecursivePower implements PowerOperation {
    private MultiplicationOperation multOp;

    public RecursivePower(MultiplicationOperation multOp) {
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
