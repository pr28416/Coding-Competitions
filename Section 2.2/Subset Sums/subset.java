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

    static int[][] dp;
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        double start = (double)System.nanoTime()/1000000000;

        int n = 0;
        BufferedReader f = new BufferedReader(new FileReader("subset.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("subset.out")));
        
        n = Integer.parseInt(f.readLine());
        System.out.println(String.format("Using N = %d", n));
        populate(n);
        out.println(answer);
        out.close();

        double end = (double)System.nanoTime()/1000000000;
        System.out.println(String.format("Program took %.6f seconds", (end-start)));
    }

    public static void populate(int N) {
        // System.out.println("Starting span");
        if (N*(N+1)/2 % 2 == 0) {
            int req = N*(N+1)/4;

            // PART 1: Create the DP 2d array and set the values of each DP position
            dp = new int[N+1][req+1];
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
            // printDP(dp);
            // System.out.println("Finished populating\nStarting span");

            // PART 2: Starting from the bottom-right corner, create sets
            span(N, dp, N, req, 0, -1);
            // System.out.println("Finished span");
            // System.out.println(e);
            answer = e;
        } else {
            // System.out.println("Ended program; result is 0");
        }
    }

    static int e = 0;

    static int sum(int[] a) {
        int w = 0;
        for (int i: a) {
            w += i;
        }
        return w;
    }

    static String toString(int[] a) {
        String w = "";
        for (int i: a) {
            w += i+" ";
        }
        return w;
    }

    public static void span(int n, int[][] dp, int node, int totalSum, int currentSum, int lastUsed) {
        // Check to see if 0 is the current spot. If so, return e+1
        // System.out.println("----");
        // System.out.println(currentSum);
        if (dp[node][totalSum] == 0) {
            if (currentSum == n*(n+1)/4) {
                // System.out.println(toString(currentSet));
                 e ++;
            }
            return;
        }

        // Check to see if you can traverse left
        if (dp[node][totalSum] >= node) {
            // Span left, increment currentSum
            if (totalSum != lastUsed) {
                span(n, dp, node, totalSum-node, currentSum+node, totalSum-node);
            }
            
        }

        // Check to see if you can traverse up
        if (node-1 >= 0 && dp[node][totalSum] == dp[node-1][totalSum] && totalSum != n*(n+1)/4) {
            // Span up
            span(n, dp, node-1, totalSum, currentSum, -1);
        }
    }

    public static void printDP(int[][] dp) {
        for (int[] i: dp) {
            for (int j: i) {
                System.out.print(j+"\t");
            }
            System.out.println();
        }
    }
}