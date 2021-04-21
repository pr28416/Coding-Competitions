import java.util.Scanner;

class Problem2 {
    static Scanner input = new Scanner(System.in);
    public static void main(String[] args) {
        System.out.println("Problem 2 - Alphabet Snake. Enter input:");
        int m = input.nextInt();
        int n = input.nextInt();
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int idx = 0;
        boolean flip = false;
        System.out.println("Answer:");
        for (int i = 0; i < n; i++) {
            String temp = "";
            for (int j = 0; j < m; j++) {
                temp += alphabet.substring(idx, idx+1);
                idx = (idx + 1) % 26;
            }
            String fin = "";
            if (flip) {
                for (int k = temp.length()-1; k >= 0; k--) {
                    fin += temp.substring(k, k+1);
                }
            } else {
                fin = temp;
            }
            System.out.println(fin);
            flip = !flip;
        }
    }
}