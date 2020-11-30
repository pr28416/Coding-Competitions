import java.util.*;

public class measurement {
    public static void main(String[] args) {
        // Get data
        Scanner input = new Scanner(System.in);

        int N = input.nextInt(), G = input.nextInt();
        int[][] entries = new int[N][3];
        for (int i = 0; i < N; i++) {
            entries[i][0] = input.nextInt();
            entries[i][1] = input.nextInt();
            entries[i][2] = input.nextInt();
        }
        input.close();

        Arrays.sort(entries, new Comparator<int[]>() {
            public int compare(final int[] a, final int[] b) {
                return a[0] - b[0];
            }
        });

        // Initial setup of production and leaderboard maps
        HashMap<Integer, Integer> production = new HashMap<Integer, Integer>();
        production.put(0, G);
        for (int[] i: entries) production.put(i[1], G);
        
        TreeMap<Integer, Integer> leaderboard = new TreeMap<Integer, Integer>();
        leaderboard.put(G, N);

        // Run through entries
        int change = 0;

        int initialMaxKey, initialMaxKeyLength;
        int initProdValue, newProdValue;

        for (int e = 0; e < entries.length; e++) {

            // Store initial max-key and its length
            initialMaxKey = leaderboard.lastKey();
            initialMaxKeyLength = leaderboard.get(initialMaxKey);

            // PART 1: Remove old value from leaderboard and production

            // Remove the number from leaderboard
            initProdValue = production.get(entries[e][1]);
            leaderboard.put(initProdValue, leaderboard.get(initProdValue)-1);

            // Remove entire object if necessary
            if (leaderboard.get(initProdValue) == 0) {
                leaderboard.remove(initProdValue);
            }
            
            // PART 2: Update new values for production and leaderboard
            
            // Change production value to new value
            production.put(entries[e][1], entries[e][2] + production.get(entries[e][1]));
            
            // Create new object for update value if necessary
            newProdValue = production.get(entries[e][1]);
            if (!leaderboard.containsKey(newProdValue)) {
                leaderboard.put(newProdValue, 0);
            }
            
            // Add new value (entries[e] key) to appropriate key (new prod value)
            leaderboard.put(newProdValue, leaderboard.get(newProdValue)+1);

            // PART 3: Check for changes

            // Check if max changed after removal
            int last = leaderboard.lastKey();
            if (last != initialMaxKey) {
                if (leaderboard.get(last) > 1) {
                    change += 1;
                } else if (initialMaxKeyLength != leaderboard.get(last) || !(newProdValue == last && initProdValue == initialMaxKey)) {
                    change += 1;
                }
            } else if (leaderboard.get(last) != initialMaxKeyLength) {
                change += 1;
            }
        }

        System.out.println(change);
    }
}