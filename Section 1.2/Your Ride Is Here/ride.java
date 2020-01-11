/*
ID: pranav.19
LANG: JAVA
TASK: ride

*/

import java.io.*;
import java.util.*;

class ride {
    public static void main(String[] args) throws IOException {
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // File file = new File("ride.in");
        // FileInputStream fis = new FileInputStream(file);
        // InputStreamReader isr = new InputStreamReader(fis);
        // BufferedReader f = new BufferedReader(isr);
        BufferedReader f = new BufferedReader(new FileReader("ride.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ride.out")));
        // StringTokenizer st = new StringTokenizer(f.readLine());

        String line1 = f.readLine();
        String line2 = f.readLine();

        // Algorithm
        int product1 = 1, product2 = 1;

        for(int i = 0; i < line1.length(); i++) {
            if (!line1.substring(i, i+1).equals("\n")) {
                product1 *= alphabet.indexOf(line1.substring(i, i+1)) + 1;
            }
        }
        for(int i = 0; i < line2.length(); i++) {
            if (!line2.substring(i, i+1).equals("\n")) {
                product2 *= alphabet.indexOf(line2.substring(i, i+1)) + 1;
            }
        }
        // System.out.println(product1 + "\t" + product2);
        // System.out.println((product1 % 47) + "\t" + (product2 % 47));

        if (product1 % 47 == product2 % 47) {
            out.println("GO");
        } else {
            out.println("STAY");
        }

        out.close();
    }
}