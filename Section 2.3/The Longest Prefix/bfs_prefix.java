/*
ID: pranav.19
LANG: JAVA
TASK: prefix
*/

import java.util.*;
import java.io.*;

class bfs_prefix {
    static ArrayList<String> primitives = new ArrayList<String>();
    static String sequence = "";
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
            if (!input.equals(".")) sequence += input;
            input = reader.readLine();
        }
        reader.close();

        System.out.println(primitives);
        System.out.println(sequence);

        bfs_span();

        System.out.println(updated);
    }

    static Set<String> updated = new HashSet<String>();

    public static void bfs_span() {
        updated.add(sequence);
        int i = 0;
        while (true) {
            System.out.println(i+"\t");
            Set<String> temp = new HashSet<String>();
            for (String seq: updated) {
                for (String prim: primitives) {
                    if (canUsePrimitive(prim, seq)) {
                        temp.add(seq.substring(prim.length()));
                        // System.out.println("\tAdding " + seq.substring(prim.length()));
                    }
                }
            }
            if (updated.containsAll(temp)) {
                // System.out.println("break");
                return;
            }
            updated = temp;
            // System.out.println(temp);
            i++;
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