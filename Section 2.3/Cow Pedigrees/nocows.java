/*
ID: pranav.19
LANG: JAVA
TASK: nocows
*/

import java.io.*;

class nocows {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File("nocows.in")));
        String[] c = reader.readLine().split(" ");
        int N = Integer.parseInt(c[0]);
        int K = Integer.parseInt(c[1]);
        System.out.println(String.format("N: %d, K: %d", N, K));
        reader.close();

        int answer = span((N-1)/2, K-1);
        System.out.println("Answer: " + answer);
    }

    public static int span(int N, int K) {

        // Create the dp
        int[][] dp = new int[N+1][K+1];

        // Pre-populate
        for (int i = 1; i < N+1 && i < K+1; i++) {
            dp[i][i] = (int)Math.pow(2, i-1);
        }

        for (int i = 1; i < N+1 && Math.pow(2, i)-1 < K+1; i++) {
            dp[(int)Math.pow(2, i)-1][i] = 1;
        }

        // Print dp
        for (int[] n: dp) {
            for (int k: n) {
                System.out.print(k+"\t");
            }
            System.out.println();
        }

        // Iterate through every element

        for (int k = 1; k < K+1; k++) {
            for (int n = k+1; n < N+1; n++) {
                if (dp[n-1][k] == 1) break;
                if (dp[n][k] == 1) break;

                // Set the value based on previous row

                int val = 0;

                for (int j = 0; j <= k; j++) {
                    val += dp[n-1][j]*(int)Math.pow(2, n-j-1);
                }

                dp[n][k] = val;


                if (val == 1 || val == 0) break;
            }
            
        }
        
        System.out.println("After");
        // Print dp
        for (int[] n: dp) {
            for (int k: n) {
                System.out.print(k+"\t");
            }
            System.out.println();
        }

        for (int i = K; i >= 0; i--) {
            if (dp[N][i] != 0) return dp[N][i];
        }
        return dp[N][K];
    }

}