package main;

public class RecursivePower implements PowerOperation {
    @Override
    public int Apply(int a, int b, MultiplicationOperation multOp) {
        if (multOp == null)
            throw new RuntimeException("MultiplicationOperation can't be null");
        if (b < 0)
            throw new RuntimeException("Power exponent can't be negative");

        if (a == 0)
            return 0;
        if (b == 0)
            return 1;

        int prevResult = this.Apply(a, b - 1, multOp);
        return multOp.Apply(a, prevResult);
    }
}
