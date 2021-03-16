import java.util.*;
import java.io.*;

public class ComfortableCows {
    
    static boolean[][] cows = new boolean[2004][2004];
    // static int[][] adj = new int[2500][2500];
    static int N;
    // static Queue<Integer[]> incompletesQueue;
    static int[][] quad = {
        new int[]{0, 1},
        new int[]{0, -1},
        new int[]{1, 0},
        new int[]{-1, 0}
    };
    static int[][] surround = {
        new int[]{-1, -1},
        new int[]{-1, 0},
        new int[]{-1, 1},
        new int[]{0, -1},
        new int[]{0, 1},
        new int[]{1, -1},
        new int[]{1, 0},
        new int[]{1, 1}
    };

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new File("prob1_silver_feb21/2.in"));
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

    public static int add(int prev, int c, int r) {
        int ans = prev;
        if (cows[r][c]) ans--;
        cows[r][c] = true;

        // incompletesQueue.clear();

        Queue<Integer[]> flood = new LinkedList<Integer[]>();
        flood.add(new Integer[]{r, c});
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

        while (!flood.isEmpty()) {
            // System.out.println(flood);
            Integer[] loc = flood.remove();
            if (adj(loc[0], loc[1]) == 3) {
                for (int[] dir: quad) {
                    if (!cows[loc[0]+dir[0]][loc[1]+dir[1]]) {
                        cows[loc[0]+dir[0]][loc[1]+dir[1]] = true;
                        flood.add(new Integer[]{loc[0]+dir[0], loc[1]+dir[1]});
                    }
                }
                // System.out.println("Added 1");
                ans++;
            }
            for (int[] dir: surround) {
                if (cows[loc[0]+dir[0]][loc[1]+dir[1]] && adj(loc[0]+dir[0], loc[1]+dir[1]) == 3) {
                    flood.add(new Integer[]{loc[0]+dir[0], loc[1]+dir[1]});
                }
            }
        }

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