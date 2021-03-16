import java.util.*;
import java.io.*;

public class SortedAdjacentDifferences {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();

        for (int t = 0; t < T; t++) {
            int n = input.nextInt();
            Integer[] a = new Integer[n]; for (int i = 0; i < n; i++) {
                a[i] = input.nextInt();
            }
            Arrays.sort(a, new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    return Math.abs(o1 - o2);
                }
            });
            for (int i = 0; i < n; i++) {
                System.out.print(a[i]);
                if (i == n-1) System.out.println();
                else System.out.print(" ");
            }
        }

        input.close();
    }
}