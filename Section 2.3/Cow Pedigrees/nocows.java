/*
ID: pranav.19
LANG: JAVA
TASK: nocows
*/

import java.io.*;
import java.util.*;

class nocows {

    static class Node {
        Node left, right;
        int height;
        String path;
        int numNodesOnPath;

        // Child node
        public Node(Node parent, char direction, int numNodesAdded) {
            height = parent.height+1;
            path = parent.path + direction;
            numNodesOnPath = parent.numNodesOnPath+numNodesAdded;
        }

        // Root node
        public Node() {
            height = 2;
            path = "V";
            numNodesOnPath = 1;
        }

        // This constructor is for copying a node's attributes to another.
        public Node(Node node) {
            this.left = node.left;
            this.right = node.right;
            this.height = node.height;
            this.path = node.path;
            this.numNodesOnPath = node.numNodesOnPath;
        }

        // String representation
        public String toString() {
            return ""+height+path;
        }
    }

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
    static int total = 0;
    static Set<String> set = new HashSet<String>();
    static Set<ArrayList<String>> lists = new HashSet<>();

    public static int span(int N, int K) {

        // Create the dp
        int[][] dp = new int[N+1][K+1];

        // Pre-populate
        for (int i = 1; i < N+1 && i < K+1; i++) {
            dp[i][i] = (int)Math.pow(2, i-1);
        }

        dp[0][0] = 1;

        // Print dp
        System.out.println("Before");
        for (int[] n: dp) {
            for (int k: n) {
                System.out.print(k+"\t");
            }
            System.out.println();
        }

        // Iterate through every element

        for (int k = 1; k < K+1; k++) {
            for (int n = k+1; n < N+1; n++) {
                // Currently at single item

                if (dp[n-1][k] == 1) break;

                int[] s = new int[n];
                for (int i = 0; i < s.length; i++) {
                    // Check row i vs row n-i
                    // Iterate through top
                    // Iterate through bottom
                    int a = 0;
                    // if (dp[i][k-1] != 0) {
                    for (int j = k-1; j >= 0; j--) {
                        // if (dp[i][j] == 0) break;
                        // System.out.println(String.format("i: %s, j: %s, k-1: %s, dp[i][j]: %s, dp[i][k-1]: %s, prod: %s", i, j, k-1, dp[i][j], dp[i][k-1], dp[i][j]*dp[i][k-1]));
                        for (int l = k-1; l >= 0; l--) {
                            a += dp[n-i][j]*dp[i][l];
                        }
                        
                    }
                    // }
                    if (n == 4 && k == 3) System.out.println(a);
                    s[i] = a;
                    // if (dp[n][n-i] != 0) {
                    //     for (int j = n-i; j >= 0; j--) {
                    //         if (dp[n][j] == 0) break;
                    //         a += dp[n][n-i]*dp[n][j];
                    //     }
                    // }
                }
                int b = 0;
                for (int i = 0; i < s.length; i++) {
                    b += s[i];
                }
                // if (n % 2 == 0) {
                //     for (int i = 0; i < s.length; i++) {
                //         b += s[i];
                //     }
                //     b *= 2;
                // } else {
                //     for (int i = 0; i < s.length-1; i++) {
                //         b += s[i];
                //     }
                //     b = b * 2 + s[s.length-1];
                // }
                dp[n][k] = b;
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