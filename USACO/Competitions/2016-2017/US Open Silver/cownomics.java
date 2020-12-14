import java.io.*;
import java.util.Scanner;
public class cownomics {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new File("cownomics.in"));
        int N = input.nextInt(), M = input.nextInt();
        String[] spotty = new String[N], plain = new String[N];
        for (int i = 0; i < N; i++) spotty[i] = input.next();
        for (int i = 0; i < N; i++) plain[i] = input.next();
        input.close();
        int count = 0;
        for (int i = 0; i < M-2; i++) {
            for (int j = i+1; j < M-1; j++) {
                outerloop: for (int k = j+1; k < M; k++) {
                    int[] marked = new int[64];
                    for (String s: spotty) {
                        marked[conv(s.charAt(i))*16+conv(s.charAt(j))*4+conv(s.charAt(k))] = 1;
                    }
                    for (String s: plain) {
                        if (marked[conv(s.charAt(i))*16+conv(s.charAt(j))*4+conv(s.charAt(k))] == 1) continue outerloop;
                    }
                    count += 1;
                }
            }
        }
        // System.out.println(count);
        PrintWriter output = new PrintWriter(new File("cownomics.out"));
        output.println(count);
        output.close();
    }

    public static int conv(char c) {
        if (c == 'A') return 0;
        if (c == 'C') return 1;
        if (c == 'G') return 2;
        return 3;
    }
}