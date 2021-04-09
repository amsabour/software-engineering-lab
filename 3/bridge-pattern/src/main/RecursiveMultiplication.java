package main;

public class RecursiveMultiplication implements MultiplicationOperation {
    @Override
    public int Apply(int a, int b) {
        if (a == 0 || b == 0)
            return 0;
        if (a == 1)
            return b;
        if (b == 1)
            return a;

        if (b < 0)
            return -1 * Apply(a, -1 * b);
        if (a < 0)
            return -1 * Apply(-1 * a, b);
        if (b < a)
            return Apply(b, a);


        int k = b / a;
        int rem = b % a;
        return k * a * a + Apply(rem, a);
    }
}
