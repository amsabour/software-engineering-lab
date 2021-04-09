package test;

import main.MultiplicationOperation;
import main.RecursiveMultiplication;
import main.SimpleMultiplication;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;


public class MultiplicationTest {
    @Test
    public void testMultiplicationCreation() {
        MultiplicationOperation multOp;
        multOp = new SimpleMultiplication();
        assertNotNull(multOp);

        multOp = new RecursiveMultiplication();
        assertNotNull(multOp);
    }

    @Test
    public void testMultiplicationCorrectness_WHEN_Simple() {
        MultiplicationOperation multOp = new SimpleMultiplication();

        for (int i = -10; i <= 10; i++) {
            for (int j = -10; j <= 10; j++) {
                assertEquals(i * j, multOp.Apply(i, j));
            }
        }
    }

    @Test
    public void testMultiplicationCorrectness_WHEN_Recursive() {
        MultiplicationOperation multOp = new RecursiveMultiplication();

        for (int i = -10; i <= 10; i++) {
            for (int j = -10; j <= 10; j++) {
                assertEquals(i * j, multOp.Apply(i, j));
            }
        }
    }
}
