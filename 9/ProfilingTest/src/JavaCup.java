import java.util.ArrayList;
import java.util.Scanner;

public class JavaCup {
    private static ArrayList<Integer> my_a;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Press number1: ");
        int i = scanner.nextInt();
        System.out.println("Press number2: ");
        int j = scanner.nextInt();
        System.out.println("Press number3: ");
        int k = scanner.nextInt();
        temp();
        eval(i, j, k);
    }

    public static void eval(int i, int j, int k) {
        if (i * i + j * j == k * k || i * i == j * j + k * k || j * j == i * i + k * k) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }


    public static void temp() {
        my_a = new ArrayList<>();
        int max = -1;
        for (int i = 0; i < 10000; i++) {
            for (int j = 0; j < 20000; j++) {
                if (i + j > max) {
                    max = i + j;
                    my_a.add(i + j);
                }
            }
        }
    }

    // Solution 1
    public static int a_get_1(int index) {
        int j = index % 20000;
        int i = (index - j) / 20000;
        return i + j;
    }

    // Solution 2
    public static int a_get_2(int index) {
        int j = index % 20000;
        int i = (index - j) / 20000;
        return my_a.get(i + j);
    }
}
