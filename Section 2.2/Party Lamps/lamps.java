/*
ID: pranav.19
LANG: JAVA
TASK: lamps
*/

import java.io.*;
import java.util.*;
public class lamps {
    static int N;
    static int C;
    static String finalState = "";
    static HashMap<String, String> allSets= new HashMap<String, String>();
    static HashMap<String, Integer> used = new HashMap<String, Integer>();
    public static void main(String[] args) throws IOException {
        runProgram();
    }

    // public static void debug() throws IOException {
    //     String t = "11111111";
    //     System.out.println("Before: "+t);
    //     t = button1(t);
    //     t = button3(t);
    //     t = button2(t);
    //     t = button4(t);
    //     System.out.println("After: "+t);
    // }

    public static void runProgram() throws IOException {
        
        System.out.println("Started");
        BufferedReader reader = new BufferedReader(new FileReader(new File("lamps3.in")));
        PrintWriter writer = new PrintWriter(new File("lamps.out"));

        N = Integer.parseInt(reader.readLine());
        C = Integer.parseInt(reader.readLine());

        String[] temp1 = reader.readLine().split(" ");
        String[] temp2 = reader.readLine().split(" ");

        int[] temp = new int[N];

        for (int i = 0; i < temp.length; i++) {
            temp[i] = 2;
        }
        for (int i = 0; i < temp1.length-1; i++) {
            temp[Integer.parseInt(temp1[i])-1] = 1;
        }
        for (int i = 0; i < temp2.length-1; i++) {
            temp[Integer.parseInt(temp2[i])-1] = 0;
        }

        for (int i: temp) {
            finalState += i;
        }


        String bulbState = "";
        for (int i = 0; i < N; i++) {
            bulbState += "1";
        }

        long startTime = System.currentTimeMillis();
        span(bulbState, 0);
        long endTime = System.currentTimeMillis();
        System.out.println(String.format("Program took %s seconds", (endTime-startTime)/1000.0));

        if (allSets.size() == 0) {
            writer.println("IMPOSSIBLE");
        } else {
            ArrayList<String> sets = new ArrayList<String>();
            for (String i: allSets.keySet()) {
                sets.add(i);
            }
            Collections.sort(sets);
            for (String i: sets) {
                writer.println(i);
            }
        }
        
        reader.close();
        writer.close();
        
    }

    public static String button1(String s) {
        String n = "";
        for (int i = 0; i < s.length(); i++) {
            n += ""+(Integer.parseInt(s.substring(i, i+1))+1)%2;
        }
        return n;
    }

    public static String button2(String s) {
        String n = "";
        for (int i = 0; i < s.length(); i++) {
            if ((i+1)%2 == 1) {
                n += ""+(Integer.parseInt(s.substring(i, i+1))+1)%2;
            } else {
                n += s.substring(i, i+1);
            }
        }
        return n;
    }

    public static String button3(String s) {
        String n = "";
        for (int i = 0; i < s.length(); i++) {
            if ((i+1)%2 == 0) {
                n += ""+(Integer.parseInt(s.substring(i, i+1))+1)%2;
            } else {
                n += s.substring(i, i+1);
            }
        }
        return n;
    }

    public static String button4(String s) {
        String n = "";
        for (int i = 0; i < s.length(); i++) {
            if (i%3 == 0) {
                n += ""+(Integer.parseInt(s.substring(i, i+1))+1)%2;
            } else {
                n += s.substring(i, i+1);
            }
        }
        return n;
    }

    public static void span(String bulbState, int c) {
        for (int i = c; i < C; i += 4) {
            if (used.containsKey(""+i+"-"+bulbState)) {
                return;
            }
        }
        if (c == C) {
            boolean noFind = true;
            for (int i = 0; i < bulbState.length(); i++) {
                if (!bulbState.substring(i, i+1).equals("2")) {
                    noFind = false;
                    break;
                }
            }
            if (noFind) {
                allSets.put(bulbState, bulbState);
                return;
            }
            // System.out.println("Trying "+bulbState);
            for (int i = 0; i < bulbState.length(); i++) {
                if (!finalState.substring(i, i+1).equals(bulbState.substring(i, i+1)) && !finalState.substring(i, i+1).equals("2")) {
                    return;
                }
            }
            // System.out.println("Worked "+bulbState);
            allSets.put(bulbState, bulbState);
            return;
        } else {
            used.put(""+c+"-"+bulbState, c);
        }
        // // Button 2+3
        // String b23 = button2(button3(bulbState));
        // span(b23, c+2);
        // Button 1
        String b1 = button1(bulbState);
        span(b1, c+1);
        // Button 2
        String b2 = button2(bulbState);
        span(b2, c+1);
        // Button 3
        String b3 = button3(bulbState);
        span(b3, c+1);
        
        // Button 4
        String b4 = button4(bulbState);
        span(b4, c+1);
        // After
        return;
    }
}