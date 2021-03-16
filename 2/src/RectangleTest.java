import org.junit.Test;
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
        Rectangle rectangle = new Rectangle(20, 11);
        assertEquals(rectangle.computeArea(), 220);
    }

    @Test
    public void testComputeArea_WHEN_heightIsLarger() {
        Rectangle rectangle = new Rectangle(20, 30);
        assertEquals(rectangle.computeArea(), 600);
    }

    @Test
    public void testComputeArea_WHEN_widthEqualsHeight() {
        Rectangle rectangle = new Rectangle(25, 25);
        assertEquals(rectangle.computeArea(), 625);
    }
}
