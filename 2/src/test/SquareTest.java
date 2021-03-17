package test;

import main.Shape;
import main.Square;
import org.junit.Test;

import static org.junit.Assert.*;


public class SquareTest {

    @Test
    public void testConstructNewSquare() {
        Square square = new Square(10);
        assertNotNull(square);
    }

    @Test
    public void testConstructNewSquare_WHEN_sideLengthIsInvalid() {
        try {
            Square square = new Square(-10);
            fail();
        } catch (Exception e) {
            assertEquals(e.getMessage(), "Square side length should be positive.");
        }

        try {
            Square square = new Square(0);
            fail();
        } catch (Exception e) {
            assertEquals(e.getMessage(), "Square side length should be positive.");
        }
    }

    @Test
    public void testComputeArea_WHEN_sideLengthIsValid() {
        for (int i = 1; i <= 10; i++) {
            Shape square = new Square(i);
            assertEquals(i * i, square.computeArea());
        }
    }

    @Test
    public void testSetSideLength_WHEN_sideLengthIsInvalid() {
        Square square = new Square(10);

        boolean threwException = false;
        try {
            square.setSideLength(-10);
        } catch (Exception e) {
            threwException = true;
        }

        assertTrue(threwException);

        threwException = false;
        try {
            square.setSideLength(0);
        } catch (Exception e) {
            threwException = true;
        }
        assertTrue(threwException);
    }

    @Test
    public void testGetSideLength_WHEN_sideLengthIsSet() {
        Square square = new Square(10);

        for (int i = 1; i <= 10; i++) {
            square.setSideLength(i);
            assertEquals(i, square.getSideLength());
        }
    }

    @Test
    public void testComputeArea_WHEN_sideLengthIsSet() {
        Square square = new Square(10);

        for (int i = 1; i <= 10; i++) {
            square.setSideLength(i);
            assertEquals(i * i, square.computeArea());
        }
    }
}
