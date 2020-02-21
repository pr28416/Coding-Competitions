/*
ID: pranav.19
LANG: JAVA
TASK: lamps
*/

import java.io.*;
import java.util.*;
public class lamps2 {
    static int N;
    static int C;
    static String orig;
    static String finalState = "";
    static Set<String> allSets= new HashSet<String>();
    static Set<String> used = new HashSet<String>();
    public static void main(String[] args) throws IOException {
        runProgram();

    }

    public static String applyCode(String code) {

        String fin = orig;
        for (String i: code.split("")) {
            if (i.equals("4")) {
                fin = button4(fin);
            } else if (i.equals("3")) {
                fin = button3(fin);
            } else if (i.equals("2")) {
                fin = button2(fin);
            } else {
                fin = button1(fin);
            }
        }
        return fin;
    }

    public static void span(String current, int c) {
        // System.out.println(current);
        if (c == 0) {
            span("1", c+1);
            span("2", c+1);
            span("3", c+1);
            span("4", c+1);
            return;
        } else if (used.contains(current)) {
            System.out.println("\t===BREAK===");
            return;
        } else if (c == C) {

            String fin = applyCode(current);

            boolean noFind = true;
            for (int i = 0; i < fin.length(); i++) {
                if (!fin.substring(i, i+1).equals("2")) {
                    noFind = false;
                    break;
                }
            }
            if (noFind) {
                allSets.add(fin);
                return;
            }

            for (int i = 0; i < fin.length(); i++) {
                if (!finalState.substring(i, i+1).equals(fin.substring(i, i+1)) && !finalState.substring(i, i+1).equals("2")) {
                    return;
                }
            }

            // System.out.println("\t===FOUND===");
            allSets.add(fin);
            return;
        } else {
            used.add(current);
            if (current.substring(current.length()-1).equals("4")) {
                span(current+"4", c+1);
            } else if (current.substring(current.length()-1).equals("3")) {
                span(current+"3", c+1);
                span(current+"4", c+1);
            } else if (current.substring(current.length()-1).equals("2")) {
                span(current+"2", c+1);
                span(current+"3", c+1);
                span(current+"4", c+1);
            } else {
                span(current+"1", c+1);
                span(current+"2", c+1);
                span(current+"3", c+1);
                span(current+"4", c+1);
            }
            return;
        }
    }

    public static void runProgram() throws IOException {
        
        System.out.println("STARTED");
        BufferedReader reader = new BufferedReader(new FileReader(new File("lamps.in")));
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
        orig = bulbState;

        long startTime = System.currentTimeMillis();
        span("", 0);
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

}