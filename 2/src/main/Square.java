package main;

public class Square {
    private int sideLength;

    public Square(int sideLength) {
        if (sideLength <= 0)
            throw new RuntimeException("Square side length should be positive.");

        this.sideLength = sideLength;
    }

    public void setSideLength(int sideLength) {
        if (sideLength <= 0)
            throw new RuntimeException("Square side length should be positive.");

        this.sideLength = sideLength;
    }

    public int getSideLength() {
        return sideLength;
    }

    public int computeArea() {
        return getSideLength() * getSideLength();
    }
}
