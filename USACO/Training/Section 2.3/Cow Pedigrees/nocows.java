/*
ID: pranav.19
LANG: JAVA
TASK: nocows
*/

import java.util.*;
import java.io.*;

class nocows {
    public static void main(String[] args) throws IOException {
        Scanner fin = new Scanner(new File("nocows.in"));
        String[] data = fin.nextLine().split(" ");

        int N = Integer.parseInt(data[0]);
        int K = Integer.parseInt(data[1]);
        long[][] dp = new long[(N-1)/2+1][K];

        dp[0][0] = 1;
        for (int n = 1; n < dp.length && n < dp[0].length; n++) {
            dp[n][n] = (long)Math.pow(2, n-1);
        }

        long answer;
        if (N % 2 == 0) {
            answer = 0;
        } else {
            alg(dp);
            answer = dp[dp.length-1][dp[0].length-1] % 9901;
        }
        PrintWriter fout = new PrintWriter(new File("nocows.out"));
        fout.println(answer);
        fout.close();
    }

    public static void alg(long[][] dp) {
        for (int N = 1; N < dp.length; N++) {
            for (int K = 1; K < dp[0].length; K++) {
                if (N == 0 || K == 0 || dp[N][K] != 0) {
                    continue;
                }

                long sum = 0;
                // 3 cases:
                // - largest depth on left, smaller on right
                for (int l = N-1; l >= 0; l--) {
                    int r = N-l-1;
                    long lh = dp[l][K-1];
                    long rh = 0;
                    for (int i = 0; i < K-1; i++) {
                        rh += dp[r][i] % 9901;
                    }
                    sum = (sum % 9901) + (lh * rh * 2) % 9901;

                    lh = dp[l][K-1] % 9901;
                    rh = dp[r][K-1] % 9901;
                    sum += (lh * rh) % 9901;
                }

                dp[N][K] = sum;
                // return sum;
            }
        }
    }

}
