import java.util.*;
import java.io.*;
public class measurement {
    public static void main(String[] args) throws FileNotFoundException {
        // Get data
        Scanner input = new Scanner(System.in);
        // Scanner input = new Scanner(new File("measurement.in"));
        int N = input.nextInt(), G = input.nextInt();
        int[][] entries = new int[N][3];
        for (int i = 0; i < N; i++) {
            entries[i] = new int[]{input.nextInt(),
                                    input.nextInt(),
                                    input.nextInt()};
        }
        input.close();
        Arrays.sort(entries, new Comparator<int[]>() {
            public int compare(final int[] a, final int[] b) {
                return a[0] - b[0];
            }
        });

        // for (int[] i: entries) System.out.println(Arrays.toString(i));

        // Initial setup of production and leaderboard maps
        HashMap<Integer, Integer> production = new HashMap<Integer, Integer>();
        production.put(0, G);
        for (int[] i: entries) production.put(i[1], G);
        
        TreeMap<Integer, HashSet<Integer>> leaderboard = new TreeMap<Integer, HashSet<Integer>>();
        HashSet<Integer> initial = new HashSet<Integer>();
        for (int[] i: entries) initial.add(i[1]);
        initial.add(0);
        leaderboard.put(G, initial);
        initial = null;
        input = null;
        
        // System.out.println(production);
        // System.out.println(leaderboard);

        // Run through entries
        int change = 0;

        for (int[] entry: entries) {
            // boolean removeChange = false;
            // boolean insertChange = false;

            // Store initial max-key and its length
            int initialMaxKey = leaderboard.lastKey();
            int initialMaxKeyLength = leaderboard.get(initialMaxKey).size();
            int initialSingleValue = -1;
            if (initialMaxKeyLength == 1) initialSingleValue = leaderboard.get(initialMaxKey).iterator().next();

            // PART 1: Remove old value from leaderboard and production

            // Remove the number from leaderboard
            int initProdValue = production.get(entry[1]);
            leaderboard.get(initProdValue).remove(entry[1]);

            // Remove entire object if necessary
            if (leaderboard.get(initProdValue).isEmpty()) {
                leaderboard.remove(initProdValue);
            }
            
            // PART 2: Update new values for production and leaderboard
            
            // Change production value to new value
            production.put(entry[1], entry[2] + production.get(entry[1]));
            
            // Create new object for update value if necessary
            int newProdValue = production.get(entry[1]);
            if (!leaderboard.containsKey(newProdValue)) {
                leaderboard.put(newProdValue, new HashSet<Integer>());
            }
            
            // Add new value (entry key) to appropriate key (new prod value)
            leaderboard.get(newProdValue).add(entry[1]);

            // PART 3: Check for changes

            // Check if max changed after removal
            int last = leaderboard.lastKey();
            if (last != initialMaxKey) {
                int newLast = leaderboard.get(last).iterator().next();
                if (leaderboard.get(last).size() > 1 || newLast != initialSingleValue) {
                    change += 1;
                    // System.out.println("New max: " + leaderboard.lastKey());
                } else {
                    // System.out.printf("There was new max but values were the same: %s and %s (from %s)\n", last, newLast, leaderboard.get(last));
                }
            }
            // Otherwise, check if max length changed
            else if (leaderboard.get(leaderboard.lastKey()).size() != initialMaxKeyLength) {
                change += 1;
                // System.out.println("Size of max changed: " + initialMaxKeyLength + " --> " + leaderboard.get(leaderboard.lastKey()).size());
            } else {
                // System.out.println("No change");
            }

            // System.out.println("\tproduction: " + production);
            // System.out.println("\tleaderboard: " + leaderboard);
            // System.out.println();
        }

        System.out.println(change);
        // PrintWriter output = new PrintWriter(new File("measurement.out"));
        // output.println(change);
        // output.close();
    }
}