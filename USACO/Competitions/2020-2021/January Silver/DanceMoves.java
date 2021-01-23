import java.util.*;
import java.io.*;

public class DanceMoves {
    public static void main(String[] args) throws IOException {
        // BufferedReader input = new BufferedReader(new FileReader(new File("DanceMoves.txt")));
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] line = input.readLine().split(" ");
        int N = Integer.parseInt(line[0]), K = Integer.parseInt(line[1]);
        int[][] swaps = new int[K][2];
        for (int i = 0; i < K; i++) {
            line = input.readLine().split(" ");
            swaps[i][0] = Integer.parseInt(line[0])-1;
            swaps[i][1] = Integer.parseInt(line[1])-1;
        }
        input.close();
        // for (int[] i: swaps) System.out.println(Arrays.toString(i));

        ArrayList<HashSet<Integer>> seen = new ArrayList<HashSet<Integer>>();
        int[] cows = new int[N];
        for (int i = 0; i < N; i++) {
            seen.add(new HashSet<Integer>());
            seen.get(i).add(i);
            cows[i] = i;
        }

        int temp;
        // int limit = 9;
        int limit = 1000000;
        for (int i = 0; i < limit; i++) {
            temp = cows[swaps[i%K][0]];
            cows[swaps[i%K][0]] = cows[swaps[i%K][1]];
            cows[swaps[i%K][1]] = temp;

            // System.out.printf("Swapping pos (%s, %s): %s\n", swaps[i%K][0], swaps[i%K][1], Arrays.toString(cows));

            seen.get(cows[swaps[i%K][0]]).add(swaps[i%K][0]);
            seen.get(cows[swaps[i%K][1]]).add(swaps[i%K][1]);
        }

        for (HashSet<Integer> i: seen) {
            System.out.println(i.size());
            // System.out.println(i);
        }
        // System.out.println("done");
    }
}
