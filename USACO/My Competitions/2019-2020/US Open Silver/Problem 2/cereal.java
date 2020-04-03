import java.io.*;
import java.util.*;

class cereal {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File("cereal.in")));
        PrintWriter writer = new PrintWriter(new File("cereal.out"));

        int N;
        int M;
        int[][] cows;

        String[] t = reader.readLine().split(" ");
        N = Integer.parseInt(t[0]);
        M = Integer.parseInt(t[1]);
        cows = new int[N][2];
        for (int i = 0; i < N; i++) {
            t = reader.readLine().split(" ");
            cows[i][0] = Integer.parseInt(t[0]); // subtract 1 to start idx at 0
            cows[i][1] = Integer.parseInt(t[1]); // subtract 1 to start idx at 0
        }

        // int[] cowsHappy = dp_alg(N, M, cows);
        // int[] cowsHappy = dp_alg2(N, M, cows);
        
        // for (int i: cowsHappy) {
        //     writer.println(i);
        // }
        int[] cowsHappy = brute_alg(N, M, cows, null);
        // writer.println();
        for (int i: cowsHappy) {
            writer.println(i);
        }
        reader.close();
        writer.close();
    }

    public static int[] dp_alg2(int N, int M, int[][] cows) {
        int[] happyCows = new int[N];
        Integer[] whoHasWhat = new Integer[M+1];

        // 0th index is for counting the angry cows
        whoHasWhat[0] = 0;

        for (int n = N-1; n >= 0; n--) {
            int idx = cows[n][0];
            int elem = cows[n][1];

            // If there is no value stored
            if (whoHasWhat[idx] == null) {
                whoHasWhat[idx] = elem;
            } else if (whoHasWhat[idx] == 0) {
                whoHasWhat[idx] = elem;
                whoHasWhat[0]++;
            }
            // If there is a value stored
            else {

                // Remember old value
                Integer oldVal = whoHasWhat[idx];
                Integer newVal = elem;
                whoHasWhat[idx] = newVal;
                
                while (true) {
                    // Take the old value at current idx, save it
                    // Replace value at current idx with new value
                    // Set the current idx to the old value
                    if (oldVal == null) {
                        whoHasWhat[idx] = newVal;
                        break;
                    } else if (oldVal == 0) {
                        whoHasWhat[idx] = newVal;
                        whoHasWhat[0]++;
                        break;
                    }
                    whoHasWhat[idx] = newVal;
                    idx = oldVal;
                    oldVal = whoHasWhat[idx];
                    newVal = 0;
                }
            }
            // for (int i = 0; i < whoHasWhat.length; i++) {
            //     System.out.print(String.format("%s: %s,   ", i, whoHasWhat[i]));
            // }
            int c = 0;
            for (int i = 1; i < whoHasWhat.length; i++) {
                if (whoHasWhat[i] != null) c++;
            }
            // System.out.println();
            happyCows[n] = c;
        }

        return happyCows;
    }

    public static int[] dp_alg(int N, int M, int[][] cows) {
        int[] happyCows = new int[N];

        HashMap<Integer, Integer> dp = new HashMap<>();

        for (int i = N-1; i >= 0; i--) {
            // If location is unvisited
            if (!dp.containsKey(cows[i][0])) {
                dp.put(cows[i][0], cows[i][1]);
            }
            // If location has been visited
            else {
                int key = cows[i][0];       // 1
                int oldVal = dp.get(key);   // 2
                dp.put(key, cows[i][1]);        // 4, 5
                while (true) {
                    if (key == oldVal) break;
                    key = oldVal;
                    if (dp.containsKey(key)) {
                        oldVal = dp.get(key);                    
                        dp.put(key, key);
                    } else {
                        dp.put(key, key);
                        break;
                    }
                    
                }
                // // Move the existing value
                // dp.put(dp.get(cows[i][0]), dp.get(cows[i][0]));
                // // Set new value
                // dp.put(cows[i][0], cows[i][1]);
            }
            happyCows[i] = dp.keySet().size();
            System.out.println(dp);
        }
        
        return happyCows;
    }

    public static int[] brute_alg(int N, int M, int[][] cows, boolean[] cereal) {
        int[] cowsHappy = new int[N];
        for (int i = 0; i < cows.length; i++) {
            int happy = 0;
            cereal = new boolean[M+1];
            for (int j = i; j < cows.length; j++) {
                // If box of favorite cereal is still available, take it and leave.
                if (cereal[cows[j][0]] == false) {
                    happy++;
                    cereal[cows[j][0]] = true;
                }
                // Else if box of second favorite cereal is still available, take it and leave.
                else if (cereal[cows[j][1]] == false) {
                    happy++;
                    cereal[cows[j][1]] = true;
                }
                // Otherwise, moo with disappointment and leave without taking any cereal.
            }
            cowsHappy[i] = happy;
        }

        return cowsHappy;
    }
}