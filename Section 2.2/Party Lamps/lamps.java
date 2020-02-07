/*
ID: pranav.19
LANG: JAVA
TASK: runround
*/

import java.io.*;
import java.util.*;
public class lamps {
    static int N;
    static int C;
    static int[] finalState;
    static ArrayList<int[]> allSets= new ArrayList<int[]>();
    public static void main(String[] args) throws IOException {
        System.out.println("Started");
        BufferedReader reader = new BufferedReader(new FileReader(new File("lamps2.in")));
        BufferedWriter writer = new BufferedWriter(new FileWriter(new File("lamps.out")));

        N = Integer.parseInt(reader.readLine());
        C = Integer.parseInt(reader.readLine());

        String[] temp1 = reader.readLine().split(" ");
        String[] temp2 = reader.readLine().split(" ");

        finalState = new int[N];
        for (int i = 0; i < finalState.length; i++) {
            finalState[i] = 2;
        }
        for (int i = 0; i < temp1.length-1; i++) {
            finalState[Integer.parseInt(temp1[i])] = 1;
        }
        for (int i = 0; i < temp2.length-1; i++) {
            finalState[Integer.parseInt(temp2[i])] = 0;
        }

        // System.out.println(Arrays.toString(finalState));
        int[] bulbState = new int[finalState.length];
        for (int i = 0; i < bulbState.length; i++) {
            bulbState[i] = 1;
        }
        span(bulbState, 0);
        for (int[] i:allSets) {
            System.out.println(Arrays.toString(i));
        }

        reader.close();
        writer.close();
    }

    public static void span(int[] bulbState, int c) {
        if (c == C) {
            for (int i = 0; i < bulbState.length; i++) {
                if (finalState[i] != bulbState[i] && finalState[i] != 2) {
                    return;
                }
            }
            allSets.add(bulbState.clone());
            return;
        }
        // Button 1
        int[] b1 = bulbState.clone();
        for (int i = 0; i < b1.length; i++) {
            b1[i] = (b1[i]+1)%2;
        }
        span(b1, c+1);
        // Button 2
        int[] b2 = bulbState.clone();
        for (int i = 0; i < b2.length; i+=2) {
            b2[i] = (b2[i]+1)%2;
        }
        span(b1, c+1);
        // Button 3
        int[] b3 = bulbState.clone();
        for (int i = 1; i < b3.length; i+=2) {
            b3[i] = (b3[i]+1)%2;
        }
        span(b3, c+1);
        // Button 4
        int[] b4 = bulbState.clone();
        for (int i = 0; i < b4.length; i+=3) {
            b4[i] = (b4[i]+1)%2;
        }
        span(b4, c+1);
        // After
        return;
    }
}