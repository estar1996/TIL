import java.util.Scanner;

public class IfElseTest {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int age = scanner.nextInt();

        if (age > 8) {
            System.out.println("학교 ㄱㄱ");
        } else {
            System.out.println("유치원 ㄱㄱ");
        }
    }
}
