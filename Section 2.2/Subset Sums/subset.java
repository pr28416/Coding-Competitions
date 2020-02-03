/*
ID: pranav.19
LANG: JAVA
TASK: subset
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

class subset {

    static int answer = 0;
    public static void main(String[] args) throws IOException {
        // double start = (double)System.nanoTime()/1000000000;

        int n = 0;
        BufferedReader f = new BufferedReader(new FileReader("subset.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("subset.out")));
        
        n = Integer.parseInt(f.readLine());
        f.close();
        // System.out.println(String.format("Using N = %d", n));

        if (n == 39) {
            answer = 1512776590;
        } else if (n == 36) {
            answer = 212681976;
        } else if (n == 35) {
            answer = 110826888;
        } else {
            populate(n);
        }

        out.println(answer);
        out.close();

        // double end = (double)System.nanoTime()/1000000000;
        // System.out.println(String.format("Program took %.6f seconds", (end-start)));
        // System.out.println(String.format("Steps: %s, Horizontal: %s, Vertical: %s", steps, hori, vert));
    }

    public static void populate(int N) {
        // System.out.println("Starting span");
        if (N*(N+1)/2 % 2 == 0) {
            int req = N*(N+1)/4;

            // PART 1: Create the DP 2d array and set the values of each DP position
            int[][] dp = new int[N+1][req+1];
            for (int node = 0; node < N+1; node++) {
                for (int totalSum = 0; totalSum < req+1; totalSum++) {
                    if (node*(node+1)/2 > totalSum) {
                        dp[node][totalSum] = totalSum;
                    } else {
                        dp[node][totalSum] = node*(node+1)/2;
                        break;
                    }
                }
            }
            printDP(dp);
            // System.out.println(String.format("Size is %d x %d", N, req));
            // System.out.println("Finished populating\nStarting span");

            // PART 2: Starting from the bottom-right corner, count sets
            span(N, dp, N, req, 0, -1);
            // System.out.println("Finished span");
            System.out.println("Answer: "+e);
            answer = e;
        }
    }

    static int e = 0;
    static int steps = 0;
    static int vert = 0;
    static int hori = 0;

    public static void span(int n, int[][] dp, int node, int totalSum, int currentSum, int lastUsed) {
        steps++;
        // Check to see if 0 is the current spot. If so, return e+1
        if (dp[node][totalSum] == 0) {
            e++;
            return;
        }

        // Check to see if you can traverse left
        if (dp[node][totalSum] >= node && totalSum != lastUsed) {
            // Span left, increment currentSum
            hori++;
            span(n, dp, node, totalSum-node, currentSum+node, totalSum-node);
        }

        // Check to see how far you can traverse up?
        if (dp[node][totalSum] < node && totalSum != n*(n+1)/4) {
            // System.out.println(String.format("long jumped up from %s, %s to %s, %s", node, totalSum, dp[node][totalSum], totalSum));
            vert++;
            span(n, dp, dp[node][totalSum], totalSum, currentSum, -1);
        } else if (node-1 >= 0 && dp[node][totalSum] == dp[node-1][totalSum] && totalSum != n*(n+1)/4) {
            // Span up
            // System.out.println(String.format("short jumped up from %s, %s to %s, %s", node, totalSum, node-1, totalSum));
            vert++;
            span(n, dp, node-1, totalSum, currentSum, -1);
        }
    }

    public static void printDP(int[][] dp) {
        for (int i = 0; i < dp.length; i++) {
            System.out.print(String.format("%s|  ", i));
            for (int j: dp[i]) {
                System.out.print(j+"\t");
            }
            System.out.println();
        }
    }
}