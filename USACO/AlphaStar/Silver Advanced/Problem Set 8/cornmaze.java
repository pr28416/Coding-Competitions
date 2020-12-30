import java.util.*;

public class cornmaze {

    static Pair[][] connections = new Pair[26][2];
    static char[][] grid;
    static Pair[][] path;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt(), M = input.nextInt();
        grid = new char[N][M];
        path = new Pair[N][M];
        int[][] visited = new int[N][M];

        Pair start = null;
        for (int i = 0; i < N; i++) {
            String line = input.next();
            for (int j = 0; j < M; j++) {
                grid[i][j] = line.charAt(j);
                path[i][j] = new Pair(i, j);

                if (grid[i][j] == '@') {
                    start = new Pair(i, j);
                    visited[i][j] = 1;
                }

                if (grid[i][j] >= 65 && grid[i][j] < 91) {
                    int idx = grid[i][j]-65;
                    if (connections[idx][0] == null) {
                        connections[idx][0] = new Pair(i, j);
                    } else {
                        connections[idx][1] = new Pair(i, j);
                        Pair a = connections[idx][0], b = connections[idx][1];
                        path[a.r][a.c] = new Pair(b.r, b.c);
                        path[b.r][b.c] = new Pair(a.r, a.c);
                    }
                }
            }
        }
        input.close();

        // for(char[] i: grid) System.out.println(Arrays.toString(i));
        // for (Pair[] i: path) System.out.println(Arrays.toString(i));
        // for (int i = 0; i < N; i++) {
        //     for (int j = 0; j < M; j++) {
        //         System.out.println(getLoc(new Pair(i, j)));
        //     }
        // }
        // System.out.println(start.r+" "+start.c);

        Queue<Pair> queue = new LinkedList<Pair>();
        queue.add(start);

        int[][] moves = {
            new int[]{-1, 0},
            new int[]{1, 0},
            new int[]{0, -1},
            new int[]{0, 1}
        };

        Pair prev = null;
        // boolean traveled = false;

        while (!queue.isEmpty()) {
            Pair item = queue.remove();

            // System.out.println("\nAt " + item);

            if (grid[item.r][item.c] == '=') {
                System.out.println(visited[item.r][item.c]-1);
                break;
            }

            for (int[] move: moves) {
                int nr = item.r+move[0], nc = item.c+move[1];
                if (nr < 0 || nr > N || nc < 0 || nc > M || grid[nr][nc] == '#') continue;
                boolean traveled = false;
                Pair dest = getLoc(nr, nc);
                if (dest.r != nr || dest.c != nc) traveled = true;
                // System.out.printf("\tTrying %s, real: %s\n", new Pair(nr, nc), dest);
                if ((visited[dest.r][dest.c] > 0 || visited[nr][nc] > 0) && !traveled) continue;
                if (visited[dest.r][dest.c] < visited[item.r][item.c]+1 && visited[dest.r][dest.c] != 0) continue;
                if (visited[nr][nc] < visited[item.r][item.c]+1 && visited[nr][nc] != 0) continue;
                visited[nr][nc] = visited[item.r][item.c]+1;
                visited[dest.r][dest.c] = visited[item.r][item.c]+1;
                // System.out.println("\tSuccess");
                queue.add(dest);
            }

            // // Try wormhole first
            // Pair end = getOtherWormhole(item);
            // if (end != null && (visited[end.r][end.c] == 0 || visited[item.r][item.c] < visited[end.r][end.c])) {
            //     visited[end.r][end.c] = visited[item.r][item.c];
            //     queue.add(end);
            //     traveled = true;
            // }
            
            // if (end == null || end != null && traveled == false && visited[item.r][item.c] != visited[prev.r][prev.c]) {
            //     // Try adjacent second
            //     for (int[] move: moves) {
            //         int nr = item.r+move[0], nc = item.c+move[1];
            //         if (nr < 0 || nr > N || nc < 0 || nc > M || grid[nr][nc] == '#') continue;
            //         if (visited[nr][nc] != 0) {
            //             if (visited[item.r][item.c]+1 >= visited[nr][nc]) {
            //                 continue;
            //             } else {
            //                 visited[nr][nc] = visited[item.r][item.c]+1; queue.add(new Pair(nr, nc));
            //             }
            //         } else {
            //             visited[nr][nc] = visited[item.r][item.c]+1; queue.add(new Pair(nr, nc));
            //         }
            //     }
            // }

            // prev = item;
        }

        // for (int[] i: visited) System.out.println(Arrays.toString(i));
    }

    static Pair getLoc(int r, int c) {
        return path[r][c];
    }

    static Pair getOtherWormhole(Pair start) {
        int idx = grid[start.r][start.c]-65;
        if (idx < 0 || idx > connections.length) return null;
        if (connections[idx][0].equals(start)) return connections[idx][1];
        return connections[idx][0];
    }

    static class Pair {
        int r, c;
        public Pair(int r, int c) {
            this.r = r;
            this.c = c;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == null) return false;
            Pair other = (Pair)obj;
            return other.r == r && other.c == c;
        }

        @Override
        public String toString() {
            return String.format("(%s, %s)", r, c);
        }
    }
}
