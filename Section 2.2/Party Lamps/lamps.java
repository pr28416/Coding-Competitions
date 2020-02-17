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
    public static void main(String[] args) throws IOException {
        // System.out.println("Started");
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

        // System.out.println(Arrays.toString(finalState));
        String bulbState = "";
        for (int i = 0; i < N; i++) {
            bulbState += "1";
        }
        // System.out.println("Final State: "+ finalState+", Bulb State: "+bulbState);
        span(bulbState, 0);
        // System.out.println("Final:");
        // for (String i:allSets) {
        //     System.out.println(i);
        // }
        if (allSets.size() == 0) {
            writer.println("IMPOSSIBLE");
        } else {
            for (String i: allSets.keySet()) {
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
        }
        // Button 1
        // int[] b1 = bulbState.clone();
        // for (int i = 0; i < b1.length; i++) {
        //     b1[i] = (b1[i]+1)%2;
        // }
        String b1 = button1(bulbState);
        span(b1, c+1);
        // Button 2
        // int[] b2 = bulbState.clone();
        // for (int i = 0; i < b2.length; i+=2) {
        //     b2[i] = (b2[i]+1)%2;
        // }
        String b2 = button2(bulbState);
        span(b2, c+1);
        // Button 3
        // int[] b3 = bulbState.clone();
        // for (int i = 1; i < b3.length; i+=2) {
        //     b3[i] = (b3[i]+1)%2;
        // }
        String b3 = button3(bulbState);
        span(b3, c+1);
        // Button 4
        // int[] b4 = bulbState.clone();
        // for (int i = 0; i < b4.length; i+=3) {
        //     b4[i] = (b4[i]+1)%2;
        // }
        String b4 = button4(bulbState);
        span(b4, c+1);
        // After
        return;
    }
}