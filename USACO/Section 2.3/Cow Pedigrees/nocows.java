/*
ID: pranav.19
LANG: JAVA
TASK: nocows
*/

import java.io.*;
class nocows {
    public static void main(String[] args) throws IOException {
        int N = 0, K = 0;
        BufferedReader reader = new BufferedReader(new FileReader(new File("nocows.in")));
        PrintWriter writer = new PrintWriter(new File("nocows.out"));

        String[] temp = reader.readLine().split(" ");
        reader.close();
        N = Integer.parseInt(temp[0]);
        K = Integer.parseInt(temp[1]);
        // System.out.println(N + " " + K);

        if (N % 2 == 0) {
            writer.println(0);
            writer.close();
            return;
        }

        int C = (N-1)/2;

        int[][] dp = new int[C+1][K+1];
        dp[0][0] = 1;
        for (int i = 1; i < C+1 && i < K+1; i++) {
            dp[i][i] = (int)Math.pow(2, i-1);
        }

        for (int i = 1; i < K+1 && (int)Math.pow(2, i)-1 < C+1; i++) {
            dp[(int)Math.pow(2, i)-1][i] = 1;
        }

        for (int[] i: dp) {
            for (int j: i) System.out.print(j+"\t");
            System.out.println();
        }

        for (int i = 1; i < dp.length; i++) {
            for (int j = 1; j < i; j++) {
                if (dp[i][j] != 0) continue;
                // Get all possible left and right subtrees
                int[] p = new int[i];
                for (int sub = 0; sub < (i+1)/2; sub++) {
                    int real = i-1-sub;
                    // Check left subtree for height
                    if (dp[real][j-1] != 0) {
                        int s = 0;
                        for (int q = 0; q <= j-1; q++) {
                            s += dp[sub][q];
                        }
                        p[sub] = dp[real][j-1]*s;
                    }
                }
                int r = 0;
                for (int a = p.length-1; a >= 0; a--) {
                    p[a] = p[p.length-a-1];
                    r += p[a];
                }
                dp[i][j] = r;
            }
        }
        
        System.out.println("\nAfter\n");
        for (int[] i: dp) {
            for (int j: i) System.out.print(j+"\t");
            System.out.println();
        }
        

        writer.close();
    }
}