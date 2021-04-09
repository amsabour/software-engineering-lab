package main;

public class SimpleMultiplication implements MultiplicationOperation {
    @Override
    public int Apply(int a, int b) {
        return a * b;
    }
}
