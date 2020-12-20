import java.util.*;
import java.io.*;

public class loan {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new File("loan.in"));
        long N = input.nextLong(), K = input.nextLong(), M = input.nextLong();
        input.close();
        // System.out.println(search(N, K, M));
        PrintWriter output = new PrintWriter(new File("loan.out"));
        output.println(search(N, K, M));
        output.close();
    }

    public static long search(long N, long K, long M) {
        long lo = 1, up = new Long("1000000000000").longValue();
        while (lo < up) {
            long y = (lo+up+1)/2;
            // System.out.println("trying " + y);
            if (simulate(N, K, M, y)) {
                // System.out.println("worked");
                lo=y;
            } else {
                // System.out.println("Didn't work");
                up=y-1;
            }
        }
        return lo;
    }

    public static boolean simulate(long N, long K, long M, long X) {
        long G = 0;
        while (K > 0 && G < N) {
            long Y = (N-G)/X;
            if (Y < M) return (N-G+M-1)/M <= K;
            long maxG = N-X*Y;
            long days = Long.min((maxG-G)/Y+1, K);
            G += Y*days;
            K -= days;
        }
        return G >= N;
    }
}
