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
        BufferedReader reader = new BufferedReader(new FileReader(new File("prefix2.in")));
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

        int l = 0;
        for (int i: answers) {
            if (i > l) {
                l = i;
            }
        }

        

        System.out.println("Answers: "+answers);
        
        writer.println(l);
        writer.close();
    }

    public static void span(String sequence, int idx) {
        for (String prim: primitives) {
            if (canUsePrimitive(prim, sequence.substring(idx))) {
                span(sequence, prim.length());
            } else {
                answers.add(seq.length()-sequence.length());
            }
        }
    }

    public static boolean canUsePrimitive(String primitive, String sequence) {
        if (primitive.length() > sequence.length()) {
            return false;
        }
        for (int i = 0; i < primitive.length(); i++) {
            if (!primitive.substring(i, i+1).equals(sequence.substring(i, i+1))) {
                return false;
            }
        }
        return true;
    }
}