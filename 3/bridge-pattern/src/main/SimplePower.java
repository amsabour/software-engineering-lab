package main;

public class SimplePower implements PowerOperation {
    @Override
    public int Apply(int a, int b, MultiplicationOperation multOp) {
        if (multOp == null)
            throw new RuntimeException("MultiplicationOperation can't be null");
        if (b < 0)
            throw new RuntimeException("Power exponent can't be negative");

        if (a == 0)
            return 0;

        int result = 1;
        for (int i = 0; i < b; i++) {
            result = multOp.Apply(result, a);
        }
        return result;
    }
}
