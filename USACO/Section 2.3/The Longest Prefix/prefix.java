/*
ID: pranav.19
LANG: JAVA
TASK: prefix
*/

import java.util.*;
import java.io.*;

class prefix {

    static List<String> primitives = new ArrayList<String>();
    // static char[] sequence;
    static StringBuilder sequence = new StringBuilder();
    static char[] newSeq;
    static int answer = 0;

    public static void main(String[] args) throws IOException {

        long st = System.nanoTime();

        BufferedReader reader = new BufferedReader(new FileReader(new File("prefix.in")));
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
            sequence.append(feed);
            feed = reader.readLine();
        }
        
        // System.out.println(seq);
        // sequence = new char[seq.length()];
        newSeq = new char[sequence.length()];
        // Arrays.fill(newSeq, ' ');
        // for (int i = 0; i < seq.length(); i++) {
        //     sequence[i] = seq.charAt(i);
        // }
        // for (char c: sequence) {
        // System.out.print(c+" ");
        // }
        // System.out.println();
        // System.out.println("done");
       
        // Span out
        span();
        writer.println(answer);
        reader.close();
        writer.close();

        long en = System.nanoTime();
        // System.out.println(String.format("Took %.7f seconds", (double) (en - st) / 100000000));
    }

    public static void span() {
        
        for (String prim : primitives) { // Worst case: 200 steps
            for (int i = 0; i < sequence.length() - prim.length() + 1; i++) { // Worst case: 200,000 steps
                if (equalSequences(i, i + prim.length(), prim)) { // Worst case: 10 steps
                    for (int j = i; j < i + prim.length(); j++) { // Worst case: 10 steps
                        newSeq[j] = prim.charAt(j - i);
                    }
                }
            }
        }
        int l = 0;
        for (char c : newSeq) { // Worst case: 200,000 steps
            if (c + ' ' == ' ')
                break;
            l++;
        }
        // System.out.println(l);
        answer = l;
        
    }

    public static boolean equalSequences(int lo, int up, String prim) { // Worst case: 10 steps
        for (int i = lo; i < up; i++) {
            if (sequence.charAt(i) != prim.charAt(i - lo)) {
                return false;
            }
        }
        return true;
    }
}