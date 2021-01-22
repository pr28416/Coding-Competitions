import java.util.*;
import java.io.*;

public class FerrisWheel {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] line = input.readLine().split(" ");
        int N = Integer.parseInt(line[0]), X = Integer.parseInt(line[1]);
        line = input.readLine().split(" ");
        int[] children = new int[N]; for (int i = 0; i < N; i++) children[i] = Integer.parseInt(line[i]);
        input.close();

        Arrays.sort(children);
        // System.out.println(Arrays.toString(children));

        int lo = 0, up = N-1;
        int c = 0;
        while (lo < up) {
            if (children[lo] + children[up] <= X) {
                lo++;
            }
            up--; c++;
        }
        if (lo == up) c++;
        System.out.println(c);
    }
}
