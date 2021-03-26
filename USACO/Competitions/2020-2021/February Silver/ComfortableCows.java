import java.util.*;
import java.io.*;

public class ComfortableCows {
    
    static boolean[][] cows = new boolean[2004][2004];
    static int[][] adj = new int[2004][2004];
    static int N;
    // static Queue<Integer[]> incompletesQueue;
    static int[][] quad = {
        new int[]{0, 1},
        new int[]{0, -1},
        new int[]{1, 0},
        new int[]{-1, 0}
    };
    // static int[][] surround = {
    //     new int[]{-1, -1},
    //     new int[]{-1, 0},
    //     new int[]{-1, 1},
    //     new int[]{0, -1},
    //     new int[]{0, 1},
    //     new int[]{1, -1},
    //     new int[]{1, 0},
    //     new int[]{1, 1}
    // };

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new File("prob1_silver_feb21/3.in"));
        // Scanner input = new Scanner(System.in);
        N = input.nextInt();
        // incompletesQueue = new LinkedList<Integer[]>();
        int prev = 0;
        for (int i = 0; i < N; i++) {
            prev = add(prev, input.nextInt()+1002, input.nextInt()+1002);
            System.out.println(prev);
        }
        input.close();
    }
    /*
    
    Get next loc to add
    If the loc that needs to be added is already there, ans--
    Add the loc to cows (bool = true)
    Update the surrounding values (in adj)
    If one of those surrounding values has a cow and it has adj value of 3:
    Add it to the queue of cows to flood
    While flood queue not empty:
    Get top item
    Find unfilled neighbor
    Fill neighbor, ans++
    For the neighbor that was added, inc itself and inc all adj of neighbors of neighbors, and check if any = 3
    If so, add that one to the queue
    
    */
    
    
    public static int add(int prev, int c, int r) {
        // Get next loc to add
        int ans = prev;
        // If the loc that needs to be added is already there, ans--
        if (cows[r][c]) ans--;
        // Add the loc to cows (bool = true)
        cows[r][c] = true;
        
        Queue<int[]> flood = new LinkedList<int[]>();
        
        // Update the surrounding values (in adj)
        int a = 0;
        for (int[] dir: quad) {
            int u = r+dir[0], v = c+dir[1];
            adj[u][v]++;

            if (cows[u][v]) {
                a++;
                // If one of those surrounding values has a cow and it has adj value of 3:
                if (adj[u][v] == 3) {
                    // Add it to the queue of cows to flood
                    flood.add(new int[]{u, v});
                }
            }
        }
        adj[r][c] = a;
        
        // While flood queue not empty:
        while (!flood.isEmpty()) {
            // Get top item
            int[] top = flood.remove();
            // Find unfilled neighbor
            int u = top[0], v = top[1];
            for (int[] dir: quad) {
                if (!cows[top[0]+dir[0]][top[1]+dir[1]]) {
                    u = top[0]+dir[0];
                    v = top[1]+dir[1];
                    break;
                }
            }
            // Fill self and neighbor, ans++
            // adj[top[0]][top[1]]++;
            cows[u][v] = true;
            ans++;
            // For the neighbor that was added, inc itself and inc all adj of neighbors of neighbors
            a = 0;
            for (int[] dir: quad) {
                adj[u+dir[0]][v+dir[1]]++;
                if (cows[u+dir[0]][v+dir[1]]) {
                    a++;
                    // Check if any = 3
                    if (adj[u+dir[0]][v+dir[1]] == 3) {
                        // If so, add that one to the queue
                        flood.add(new int[]{u+dir[0], v+dir[1]});
                    }
                }
            }
            adj[u][v] = a;
        }
        
        
        // flood.add(new int[]{r, c});
        // while (!flood.isEmpty()) {
        //     Integer[] loc = flood.remove();
        //     if (adj(loc[0], loc[1]) == 3) {
        //         incompletesQueue.add(new Integer[]{loc[0], loc[1]});
        //     }
        //     for (int[] dir: directions) {
        //         if (cows[loc[0]+dir[0]][loc[1]+dir[1]]) {
        //             flood.add(new Integer[]{loc[0]+dir[0], loc[1]+dir[1]});
        //         }
        //     }
        // }

        // while (!flood.isEmpty()) {
        //     // System.out.println(flood);
        //     Integer[] loc = flood.remove();
        //     if (adj(loc[0], loc[1]) == 3) {
        //         for (int[] dir: quad) {
        //             if (!cows[loc[0]+dir[0]][loc[1]+dir[1]]) {
        //                 cows[loc[0]+dir[0]][loc[1]+dir[1]] = true;
        //                 flood.add(new Integer[]{loc[0]+dir[0], loc[1]+dir[1]});
        //             }
        //         }
        //         // System.out.println("Added 1");
        //         ans++;
        //     }
        //     for (int[] dir: surround) {
        //         if (cows[loc[0]+dir[0]][loc[1]+dir[1]] && adj(loc[0]+dir[0], loc[1]+dir[1]) == 3) {
        //             flood.add(new Integer[]{loc[0]+dir[0], loc[1]+dir[1]});
        //         }
        //     }
        // }

        return ans;
    }

    public static int adj(int r, int c) {
        int a = 0;
        for (int[] dir: quad) {
            if (cows[r+dir[0]][c+dir[1]]) a++;
        }
        return a;
    }
}