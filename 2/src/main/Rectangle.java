package main;

public class Rectangle {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        if (width <= 0)
            throw new RuntimeException("Width should be positive.");
        if (height <= 0)
            throw new RuntimeException("Height should be positive.");
        this.width = width;
        this.height = height;
    }

    public void setWidth(int width) {
        if (width <= 0)
            throw new RuntimeException("Width should be positive.");

        this.width = width;
    }

    public void setHeight(int height) {
        if (height <= 0)
            throw new RuntimeException("Height should be positive.");

        this.height = height;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public int computeArea() {
        return getWidth() * getHeight();
    }
}
