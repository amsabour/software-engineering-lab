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

    public int computeArea() {
        return width * height;
    }

    public void setWidth(int width) {
    }

    public void setHeight(int height) {

    }

    public int getWidth() {
        return 0;
    }

    public int getHeight() {
        return 0;
    }
}
