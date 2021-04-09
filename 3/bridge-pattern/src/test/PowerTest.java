package test;

import main.*;
import org.junit.Test;

import static org.junit.Assert.*;


public class PowerTest {
    @Test
    public void testPowerCreation() {
        MultiplicationOperation multOp = new SimpleMultiplication();
        PowerOperation powerOp;
        powerOp = new SimplePower();
        assertNotNull(powerOp);

        powerOp = new RecursivePower();
        assertNotNull(powerOp);
    }

    @Test
    public void testPowerCorrectness_WHEN_Simple() {
        MultiplicationOperation simpleMultOp = new SimpleMultiplication();
        MultiplicationOperation recursiveMultOp = new RecursiveMultiplication();

        PowerOperation simplePowerOp = new SimplePower();

        SimpleCheckPowerCorrectness(simplePowerOp, simpleMultOp);
        SimpleCheckPowerCorrectness(simplePowerOp, recursiveMultOp);
    }

    @Test
    public void testPowerCorrectness_WHEN_Recursive() {
        MultiplicationOperation simpleMultOp = new SimpleMultiplication();
        MultiplicationOperation recursiveMultOp = new RecursiveMultiplication();

        PowerOperation recursivePowerOp = new RecursivePower();


        SimpleCheckPowerCorrectness(recursivePowerOp, simpleMultOp);
        SimpleCheckPowerCorrectness(recursivePowerOp, recursiveMultOp);
    }

    @Test
    public void testPowerCorrectness_WHEN_Zero() {
        MultiplicationOperation multOp = new SimpleMultiplication();
        PowerOperation simplePowerOp = new SimplePower();
        PowerOperation recursivePowerOp = new RecursivePower();

        for (int i = 0; i < 100; i++) {
            assertEquals(0, simplePowerOp.Apply(0, i, multOp));
            assertEquals(0, recursivePowerOp.Apply(0, i, multOp));

            if (i > 0) {
                assertEquals(1, simplePowerOp.Apply(i, 0, multOp));
                assertEquals(1, recursivePowerOp.Apply(i, 0, multOp));
            }
        }
    }

    @Test
    public void testPowerError_WHEN_NegativeExponent() {
        MultiplicationOperation multOp = new SimpleMultiplication();
        PowerOperation simplePowerOp = new SimplePower();
        PowerOperation recursivePowerOp = new RecursivePower();

        for (int i = -10; i <= 10; i++) {
            for (int j = 1; j <= 10; j++) {
                try {
                    simplePowerOp.Apply(i, j * -1, multOp);
                    fail();
                } catch (RuntimeException ignored) {

                }
                try {
                    recursivePowerOp.Apply(i, j * -1, multOp);
                    fail();
                } catch (RuntimeException ignored) {

                }
            }
        }
    }


    private int basePower(int a, int b) {
        if (a == 0)
            return 0;
        if (b == 0)
            return 1;
        int result = 1;
        for (int i = 0; i < b; i++) {
            result *= a;
        }
        return result;
    }

    private void SimpleCheckPowerCorrectness(PowerOperation powerOp, MultiplicationOperation multOp) {
        for (int i = -10; i <= 10; i++) {
            for (int j = 0; j <= 10; j++) {
                int result = basePower(i, j);
                assertEquals(result, powerOp.Apply(i, j, multOp));
            }
        }
    }
}
