package test;

import main.Rectangle;
import main.Shape;
import org.junit.Test;

import java.util.Random;

import static org.junit.Assert.*;

public class RectangleTest {

    @Test
    public void testConstructNewRectangle() {
        Rectangle rectangle = new Rectangle(10, 20);
        assertNotNull(rectangle);
    }

    @Test
    public void testConstructNewRectangle_WHEN_widthIsNegative() {
        try {
            Rectangle rectangle = new Rectangle(-10, 20);
            fail();
        } catch (Exception e) {
            assertEquals(e.getMessage(), "Width should be positive.");
        }
    }

    @Test
    public void testConstructNewRectangle_WHEN_heightIsNegative() {
        try {
            Rectangle rectangle = new Rectangle(20, 0);
            fail();
        } catch (Exception e) {
            assertEquals(e.getMessage(), "Height should be positive.");
        }
    }

    @Test
    public void testComputeArea_WHEN_widthIsLarger() {
        Shape rectangle = new Rectangle(20, 11);
        assertEquals(rectangle.computeArea(), 220);
    }

    @Test
    public void testComputeArea_WHEN_heightIsLarger() {
        Shape rectangle = new Rectangle(20, 30);
        assertEquals(rectangle.computeArea(), 600);
    }

    @Test
    public void testComputeArea_WHEN_widthEqualsHeight() {
        Shape rectangle = new Rectangle(25, 25);
        assertEquals(rectangle.computeArea(), 625);
    }

    @Test
    public void testSetWidth_WHEN_widthIsInvalid() {
        Rectangle rectangle = new Rectangle(10, 10);

        boolean threwException = false;
        try {
            rectangle.setWidth(-10);
        } catch (Exception e) {
            threwException = true;
        }

        assertTrue(threwException);

        threwException = false;
        try {
            rectangle.setWidth(0);
        } catch (Exception e) {
            threwException = true;
        }
        assertTrue(threwException);
    }

    @Test
    public void testGetWidth_WHEN_widthIsSet() {
        Rectangle rectangle = new Rectangle(10, 20);
        assertEquals(10, rectangle.getWidth());

        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            int randomWidth = random.nextInt(1000) + 1;
            rectangle.setWidth(randomWidth);

            assertEquals(randomWidth, rectangle.getWidth());
            assertEquals(20, rectangle.getHeight());
        }
    }

    @Test
    public void testSetHeight_WHEN_heightIsInvalid() {
        Rectangle rectangle = new Rectangle(10, 120);

        boolean threwException = false;
        try {
            rectangle.setHeight(-13);
        } catch (Exception e) {
            threwException = true;
        }

        assertTrue(threwException);

        threwException = false;
        try {
            rectangle.setHeight(0);
        } catch (Exception e) {
            threwException = true;
        }
        assertTrue(threwException);
    }

    @Test
    public void testGetHeight_WHEN_heightIsSet() {
        Rectangle rectangle = new Rectangle(10, 20);
        assertEquals(20, rectangle.getHeight());

        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            int randomHeight = random.nextInt(1000) + 1;
            rectangle.setHeight(randomHeight);

            assertEquals(randomHeight, rectangle.getHeight());
            assertEquals(10, rectangle.getWidth());
        }
    }

    @Test
    public void testComputeArea_WHEN_widthAndHeightAreSet() {
        Rectangle rectangle = new Rectangle(10, 20);

        assertEquals(200, rectangle.computeArea());
        assertEquals(10, rectangle.getWidth());
        assertEquals(20, rectangle.getHeight());

        Random random = new Random();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                int randomWidth = random.nextInt(1000) + 1;
                int randomHeight = random.nextInt(1000) + 1;

                rectangle.setWidth(randomWidth);
                rectangle.setHeight(randomHeight);

                assertEquals(randomWidth, rectangle.getWidth());
                assertEquals(randomHeight, rectangle.getHeight());
                assertEquals(randomWidth * randomHeight, rectangle.computeArea());
            }
        }
    }
}
