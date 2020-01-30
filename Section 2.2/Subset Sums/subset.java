class Subset {

    static int[][] dp;
    int answer = 0;
    public static void main(String[] args) {
        int n = 7;
        populate(n);
    }

    public static void populate(int N) {
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
            printDP(dp);

            // PART 2: Starting from the bottom-right corner, create sets
            span(N, dp, N, req, 0);
            System.out.println(e);
        }
    }

    static int e = 0;

    public static void span(int n, int[][] dp, int node, int totalSum, int currentSum) {
        // Check to see if 0 is the current spot. If so, return e+1
        System.out.println("----");
        System.out.println(currentSum);
        if (dp[node][totalSum] == 0) {
            if (currentSum == n*(n+1)/4) {
                 e ++;
            }
            return;
        }

        // Check to see if you can traverse left
        if (dp[node][totalSum] >= node) {
            // Span left, increment currentSum
            span(n, dp, node, totalSum, currentSum+node);
        }

        // Check to see if you can traverse up
        if (node-1 >= 0 && dp[node][totalSum] == dp[node-1][totalSum] && totalSum != n*(n+1)/4) {
            // Span up
            span(n, dp, node-1, totalSum, currentSum);
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