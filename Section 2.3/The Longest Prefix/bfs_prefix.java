/*
ID: pranav.19
LANG: JAVA
TASK: prefix
*/

import java.util.*;
import java.io.*;

class bfs_prefix {

    static List<String> primitives = new ArrayList<String>();
    static String sequence = "";
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        /**
         * Read prefix.in
         * Get the list of primitives
         * Get the full sequence
         * BFS span
         */

         BufferedReader reader = new BufferedReader(new FileReader(new File("prefix.in")));
         PrintWriter writer = new PrintWriter(new File("prefix.out"));

         String feed = reader.readLine();

         // Add all the primitives
         
         while (!feed.equals(".")) {
             String[] temp = feed.split(" ");
             for (String t: temp) {
                primitives.add(t);
             }
             feed = reader.readLine();
         }
         feed = reader.readLine();

         // Concatenate the rest of the file into the sequence
         while (feed != null) {
             sequence += feed;
             feed = reader.readLine();
         }

         // Span out
         span();
         writer.println(answer);
         reader.close();
         writer.close();
    }

    public static void span() {
        HashSet<String> possibleSequences = new HashSet<String>();
        possibleSequences.add(sequence);
        while (true) {
            // System.out.println(possibleSequences.size());
            HashSet<String> temp = new HashSet<String>();
            for (String seq: possibleSequences) {
                for (String prim: getPrimitivesForSequence(seq)) {
                    temp.add(seq.substring(prim.length()));
                }
            }
            if (temp.size() == 0) {
                break;
            } else {
                possibleSequences = temp;
            }
        }
        for (String seq: possibleSequences) {
            if (sequence.length()-seq.length() > answer) {
                answer = sequence.length()-seq.length();
            }
        }
        // System.out.println(answer);
    }

    public static Set<String> getPrimitivesForSequence(String seq) {
        Set<String> h = new HashSet<>();
        for (String prim: primitives) {
            if (prim.length() <= seq.length()) {
                boolean b = true;
                for (int i = 0; i < prim.length(); i++) {
                    if (!seq.substring(i, i+1).equals(prim.substring(i, i+1))) {
                        b = false; break;
                    }
                }
                if (b) {
                    h.add(prim);
                }
            }
        }
        return h;
    }
}