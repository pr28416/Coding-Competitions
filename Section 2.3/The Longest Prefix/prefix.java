/*
ID: pranav.19
LANG: JAVA
TASK: prefix
*/

import java.util.*;
import java.io.*;

class prefix {

    static List<String> primitives = new ArrayList<String>();
    static String sequence = "";
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        /**
         * Read prefix.in Get the list of primitives Get the full sequence BFS span
         */
        // System.out.println("start");
        BufferedReader reader = new BufferedReader(new FileReader(new File("prefix2.in")));
        PrintWriter writer = new PrintWriter(new File("prefix.out"));

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
            sequence += feed;
            feed = reader.readLine();
        }

        // Span out
        span();
        // System.out.println(answer);
        writer.println(answer);
        reader.close();
        writer.close();
    }

    public static void span() {
        HashSet<String> seqUsed = new HashSet<String>();
        seqUsed.add("");
        while (true) {
            HashSet<String> temp = new HashSet<String>();
            System.out.println(seqUsed.size());
            boolean b = true;
            for (String seq: seqUsed) {
                for (String prim: primitives) {
                    if (seq.length() + prim.length() <= sequence.length() &&
                    (seq+prim).equals(sequence.substring(0, seq.length()+prim.length()))) {
                        // System.out.println("adding "+prim+" to "+seq+" ==> "+seq+prim);
                        temp.add(seq+prim);
                        b = false;
                    }
                }
            }
            
            
            if (b) {
                int l = 0;
                for (String t: seqUsed) {
                    if (t.length() > l) {
                        l = t.length();
                    }
                }
                // System.out.println(l);
                answer = l;
                return;
            } else {
                seqUsed = temp;
            }
        }
    }

    // public static void span() {
    //     HashSet<String> possibleSequences = new HashSet<String>();
    //     // String mySeq = "";
    //     possibleSequences.add(sequence);
    //     while (true) {
    //         // System.out.println(possibleSequences.size());
    //         HashSet<String> temp = new HashSet<String>();
    //         for (String seq : possibleSequences) {
    //             // for (String prim : getPrimitivesForSequence(seq)) {
    //             // temp.add(seq.substring(prim.length()));
    //             // }
    //             for (String prim : primitives) {
    //                 if (prim.length() <= seq.length()) {
    //                     if (seq.substring(0, prim.length()).equals(prim)) {
    //                         // h.add(prim);
    //                         temp.add(seq.substring(prim.length()));
    //                     }
    //                 }
    //             }
    //         }
    //         if (temp.size() == 0) {
    //             break;
    //         } else {
    //             possibleSequences = temp;
    //         }
    //         // System.out.println(mySeq);

    //         // String primUsed = "";

    //         // for (String prim: primitives) {
    //         // if (mySeq.length() + prim.length() <= sequence.length() &&
    //         // (mySeq+prim).equals(sequence.substring(0, mySeq.length()+prim.length())) &&
    //         // prim.length() > primUsed.length()) {
    //         // primUsed = prim;
    //         // }
    //         // }
    //         // if (mySeq.equals(mySeq+primUsed)) {
    //         // answer = mySeq.length();
    //         // break;
    //         // } else {
    //         // mySeq += primUsed;
    //         // }
    //         // }
    //         // for (String seq : possibleSequences) {
    //         // if (sequence.length() - seq.length() > answer) {
    //         // answer = sequence.length() - seq.length();
    //         // }
    //         // }

    //     }
    // }

}