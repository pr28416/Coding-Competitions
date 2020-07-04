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
    static Set<String> allSets= new HashSet<String>();
    static Set<String> used = new HashSet<String>();
    public static void main(String[] args) throws IOException {
        runProgram();
    }

    public static void runProgram() throws IOException {
        
        System.out.println("STARTED");
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
        span(bulbState, 0, 1, 0);
        
        long endTime = System.currentTimeMillis();
        System.out.println(String.format("Program took %s seconds", (endTime-startTime)/1000.0));

        if (allSets.size() == 0) {
            writer.println("IMPOSSIBLE");
        } else {
            ArrayList<String> sets = new ArrayList<String>();
            for (String i: allSets) {
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
            // THIS IS WHERE THE ERROR IS OCCURRING!!!!
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

    public static void span(String bulbState, int c, int lastUsed, int depth) {
        System.out.print(depth+"\t");
        for (int i = c; i < C; i += 4) {
            if (used.contains(""+i+"-"+bulbState)) {
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
                allSets.add(bulbState);
                return;
            }
            // System.out.println("Trying "+bulbState);
            for (int i = 0; i < bulbState.length(); i++) {
                if (!finalState.substring(i, i+1).equals(bulbState.substring(i, i+1)) && !finalState.substring(i, i+1).equals("2")) {
                    return;
                }
            }
            allSets.add(bulbState);
            return;
        } else {
            used.add(""+c+"-"+bulbState);
        }
        String b1 = "";
        try {
            b1 = button1(bulbState);
        } catch (Exception e) {
            System.out.println("ERROR ERROR: "+e.getLocalizedMessage());
        }
        
        String b2 = button2(bulbState);
        String b3 = button3(bulbState);
        String b4 = button4(bulbState);

        if (lastUsed == 4) {
            span(b4, c+1, 4, depth+1);
        } else if (lastUsed == 3) {
            span(b3, c+1, 3, depth+1);
            span(b4, c+1, 4, depth+1);
        } else if (lastUsed == 2) {
            span(b2, c+1, 2, depth+1);
            span(b3, c+1, 3, depth+1);
            span(b4, c+1, 4, depth+1);
        } else {
            span(b1, c+1, 1, depth+1);
            span(b2, c+1, 2, depth+1);
            span(b3, c+1, 3, depth+1);
            span(b4, c+1, 4, depth+1);
        }       
        
        // After
        return;
    }
}