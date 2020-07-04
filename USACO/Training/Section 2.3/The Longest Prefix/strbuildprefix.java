/*
ID: pranav.19
LANG: JAVA
TASK: prefix
*/

import java.util.*;
import java.io.*;

class prefix {

    static List<String> primitives = new ArrayList<String>();
    static StringBuilder sequence = new StringBuilder();
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        /**
         * Read prefix.in Get the list of primitives Get the full sequence BFS span
         */
        // System.out.println("start");
        long st = System.nanoTime();
        BufferedReader reader = new BufferedReader(new FileReader(new File("prefix.in")));
        PrintWriter writer = new PrintWriter(new File("prefix.out"));
        System.out.println("Java "+System.getProperty("java.version"));

        String feed = reader.readLine();

        // Add all the primitives

        while (!feed.equals(".")) {
            String[] temp = feed.split(" ");
            for (String t : temp) {
                primitives.add(t);
            }
            feed = reader.readLine();
        }
        feed = reader.readLine();

        // Concatenate the rest of the file into the sequence
        while (feed != null) {
            sequence.append(feed);
            feed = reader.readLine();
        }
        // System.out.println("Finished getting input");
        // Span out
        span();
        // System.out.println(answer);
        writer.println(answer);
        reader.close();
        writer.close();
        long en = System.nanoTime();
        System.out.println(String.format("%.7f seconds", (double)(en-st)/1000000000));
    }

    public static void span() {
        StringBuilder[][] dp = new StringBuilder[sequence.length()][primitives.size()];
        StringBuilder visibleSeq = new StringBuilder(sequence.length());
        StringBuilder largestSeq = new StringBuilder();
        for (int row = 0; row < dp.length; row++) {
            // Add next character to visibleSeq so it too is visible for comparison.
            visibleSeq.append(sequence.charAt(row));
            StringBuilder s = new StringBuilder();
            for (int col = 0; col < primitives.size(); col++) {
                if (row != 0) {
                    dp[row][col] = new StringBuilder(dp[row-1][col]);
                } else {
                    dp[row][col] = new StringBuilder();
                }
                
                // int l = dp[row][col].length();
                dp[row][col].append(primitives.get(col));

                if (dp[row][col].compareTo(visibleSeq) == 0) {
                    // We good
                } else {
                    // dp[row][col].delete(l, dp[row][col].length());
                    dp[row][col] = new StringBuilder(largestSeq);
                }
                
                if (dp[row][col].length() > s.length()) {
                    s = dp[row][col];
                }

                // System.out.print(dp[row][col]+"\t");
            }

            largestSeq = s;
            // System.out.println();
            // System.out.println("*** new largest seq will be "+largestSeq);
        }
        // System.out.println("Final:");
        // for (StringBuilder[] t: dp) {
        //     for (StringBuilder s: t) {
        //         System.out.print(s+"\t");
        //     }
        //     System.out.println();
        // }
        
        // System.out.println();
        // System.out.println(visibleSeq.length()); // Use for testing time complexity of algorithm
        answer = largestSeq.length();
        // System.out.println(answer);
    }

}