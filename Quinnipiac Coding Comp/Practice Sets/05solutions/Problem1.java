import java.util.Scanner;

class Problem1 {
    static Scanner input = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Problem 1 - Adding consecutive numbers. Enter input:");
        int n = input.nextInt();
        int m = input.nextInt();
        int l = 0, s = 0;
        if (n > m) {
            l = n;
            s = m;
        } else {
            l = m;
            s = n;
        }
        int sum = 0;
        for (int i = s; i <= l; i++) {
            sum += i;
        }
        System.out.println("Answer:");
        System.out.println(sum);
    }
}