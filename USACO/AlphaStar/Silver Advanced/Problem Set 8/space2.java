import java.util.*;

public class space2 {

    // static void flood(int i, int j, int k) {
    //     if (i < 0 || i >= N || j < 0 || j >= N || grid[i][j] != '*' || visited[i][j] != 0) return;
    //     visited[i][j] = k;
    //     for (int[] move: moves) {
    //         flood(i+move[0], j+move[1], k);
    //     }
    // }
    
    static int[][] moves = {
        new int[]{-1, 0},
        new int[]{1, 0},
        new int[]{0, -1},
        new int[]{0, 1}
    };
    static char[][] grid;
    static int[][] visited;
    static int N;
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        N = input.nextInt();
        
        grid = new char[N][N];
        visited = new int[N][N];
        Collection<Pair> asteroids = new LinkedList<Pair>();
        
        for (int i = 0; i < N; i++) {
            String line = input.next();
            for (int j = 0; j < N; j++) {
                grid[i][j] = line.charAt(j);
                if (grid[i][j] == '*') {
                    asteroids.add(new Pair(i, j));
                }
            }
        }

        input.close();

        // int k = 0;
        // for (Pair start: asteroids) {
        //     if (visited[start.r][start.c] != 0) continue;
        //     flood(start.r, start.c, ++k);
        // }

        // System.out.println(k);
        // for (int[] i: visited) System.out.println(Arrays.toString(i));

        Queue<Pair> queue = new LinkedList<Pair>();

        // System.out.println("Grid:");
        // for (char[] i: grid) System.out.println(Arrays.toString(i));
        
        int k = 0;
        for (Pair start: asteroids) {
            if (visited[start.r][start.c] != 0) continue;
            k += 1;
            visited[start.r][start.c] = k;
            queue.add(start);
            
            while (!queue.isEmpty()) {
                Pair item = queue.remove();
                for (int[] move: moves) {
                    int nr = item.r+move[0], nc = item.c+move[1];
                    if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                    if (visited[nr][nc] != 0 || grid[nr][nc] != '*') continue;
                    visited[nr][nc] = k;
                    queue.add(new Pair(nr, nc));
                }
            }
            
            queue.clear();
        }
        
        System.out.println(k);
        // System.out.println("Visited:");
        // for (int[] i: visited) System.out.println(Arrays.toString(i));
    }

    static class Pair {
        int r, c;
        public Pair(int _r, int _c) {r = _r; c = _c;}
    }
}
