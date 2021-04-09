package test;

import main.*;
import org.junit.Test;

import static org.junit.Assert.*;


public class PowerTest {

    @Test
    public void testPowerCreation_WHEN_InputNotNull() {
        MultiplicationOperation multOp = new SimpleMultiplication();
        PowerOperation powerOp;
        powerOp = new SimplePower(multOp);
        assertNotNull(powerOp);

        powerOp = new RecursivePower(multOp);
        assertNotNull(powerOp);
    }

    @Test
    public void testPowerCreation_WHEN_InputIsNull() {
        try {
            new SimplePower(null);
            fail();
        } catch (Exception ignored) {

        }

        try {
            new RecursivePower(null);
            fail();
        } catch (Exception ignored) {
        }
    }

    @Test
    public void testPowerCorrectness_WHEN_Simple() {
        PowerOperation powerOp = new SimplePower(new SimpleMultiplication());

        for (int i = -10; i <= 10; i++) {
            for (int j = 0; j <= 10; j++) {
                assertEquals((int) Math.pow(i, j), powerOp.Apply(i, j));
            }
        }
    }

    @Test
    public void testPowerCorrectness_WHEN_Recursive() {
        PowerOperation powerOp = new RecursivePower(new SimpleMultiplication());

        for (int i = -10; i <= 10; i++) {
            for (int j = 0; j <= 10; j++) {
                assertEquals((int) Math.pow(i, j), powerOp.Apply(i, j));
            }
        }
    }

    @Test
    public void testPowerCorrectness_WHEN_Zero() {
        PowerOperation simplePowerOp = new SimplePower(new SimpleMultiplication());
        PowerOperation recursivePowerOp = new RecursivePower(new SimpleMultiplication());

        for (int i = 0; i < 100; i++) {
            assertEquals(0, simplePowerOp.Apply(0, i));
            assertEquals(0, recursivePowerOp.Apply(0, i));

            assertEquals(1, simplePowerOp.Apply(i, 0));
            assertEquals(1, recursivePowerOp.Apply(i, 0));
        }
    }

    @Test
    public void testPowerError_WHEN_NegativeExponent() {
        PowerOperation simplePowerOp = new SimplePower(new SimpleMultiplication());
        PowerOperation recursivePowerOp = new RecursivePower(new SimpleMultiplication());

        for (int i = -10; i <= 10; i++) {
            for (int j = -1; j >= -10; j--) {
                try {
                    simplePowerOp.Apply(i, j);
                    fail();
                } catch (RuntimeException ignored) {

                }
                try {
                    recursivePowerOp.Apply(i, j);
                    fail();
                } catch (RuntimeException ignored) {

                }
            }
        }
    }

    @Test
    public void testPowerCorrectness_WHEN_SwitchMultOp() {
        MultiplicationOperation simpleMultOp = new SimpleMultiplication();
        MultiplicationOperation recursiveMultOp = new RecursiveMultiplication();

        PowerOperation simplePowerOp = new SimplePower(simpleMultOp);
        PowerOperation recursivePowerOp = new RecursivePower(simpleMultOp);

        for (int i = -10; i < 10; i++) {
            for (int j = 0; j <= 10; j++) {
                int result = (int) Math.pow(i, j);
                simplePowerOp.SetMultOp(simpleMultOp);
                recursivePowerOp.SetMultOp(simpleMultOp);

                assertEquals(result, simplePowerOp.Apply(i, j));
                assertEquals(result, recursivePowerOp.Apply(i, j));

                simplePowerOp.SetMultOp(recursiveMultOp);
                recursivePowerOp.SetMultOp(recursiveMultOp);

                assertEquals(result, simplePowerOp.Apply(i, j));
                assertEquals(result, recursivePowerOp.Apply(i, j));
            }
        }
    }
}
