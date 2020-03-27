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
                // Set the value based on previous row

                int val = 0;

                for (int j = 0; j <= k; j++) {
                    val += dp[n-1][j]*(int)Math.pow(2, n-j);
                }

                dp[n][k] = val/2;


                if (val/2 == 1 && val/2 == 0) {
                    break;
                }
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