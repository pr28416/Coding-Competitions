/*
ID: pranav.19
LANG: JAVA
TASK: prefix
*/

import java.util.*;
import java.io.*;

class prefix {

    static ArrayList<String> primitives = new ArrayList<String>();
    static Set<Integer> answers = new HashSet<Integer>();
    static String seq = "";
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File("prefix.in")));
        PrintWriter writer = new PrintWriter(new File("prefix.out"));

        
        String input = reader.readLine();
        while (!input.equals(".")) {
            String[] temp = input.split(" ");
            for (String i: temp) {
                primitives.add(i);
            }
            input = reader.readLine();
        }
        while (input != null) {
            if (!input.equals(".")) seq += input;
            input = reader.readLine();
        }
        reader.close();

        System.out.println(primitives);
        System.out.println(seq);


        span(seq, 0);
        // for (String p: primitives) {
        //     System.out.println(canUsePrimitive(p, seq, 5));
        // }

        // int l = 0;
        // for (int i: answers) {
        //     if (i > l) {
        //         l = i;
        //     }
        // }

        // System.out.println("Answers: "+answers);
        
        // writer.println(largest);
        writer.close();
    }

    // static int largest = 0;

    public static void span(String sequence, int idx) {
        System.out.println(sequence.substring(idx)+"\t"+idx);
        for (String prim: primitives) {
            if (canUsePrimitive(prim, sequence, idx)) {
                span(sequence, prim.length());
            } else {
                answers.add(seq.length()-sequence.length());
                System.out.println("adding");
            }
        }
    }

    public static boolean canUsePrimitive(String primitive, String sequence, int idx) {
        if (primitive.length() > (sequence.length()-idx)) {
            return false;
        }
        for (int i = 0; i < primitive.length(); i++) {
            if (!primitive.substring(i, i+1).equals(sequence.substring(i+idx, i+1+idx))) {
                return false;
            }
        }
        return true;
    }
}