import java.util.*;

public class lphone {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int W = input.nextInt(), H = input.nextInt();
        char[][] grid = new char[H][W];
        int[][] visited = new int[H][W];
        int cI = -1, cJ = -1;
        int endI = -1, endJ = -1;
        for (int i = 0; i < H; i++) {
            String e = input.next();
            for (int j = 0; j < W; j++) {
                grid[i][j] = e.charAt(j);
                if (grid[i][j] == 'C') {
                    if (cI == -1 && cJ == -1) {
                        cI = i; cJ = j;
                    } else {
                        endI = i; endJ = j;
                    }
                }
            }
        }
        input.close();

        Queue<Move> queue = new LinkedList<Move>();
        queue.add(new Move(cI, cJ, -1));

        int mirrors = Integer.MAX_VALUE;
        while (!queue.isEmpty()) {
            Move item = queue.remove();
            if (item.r == endI && item.c == endJ) {
                mirrors = Integer.min(mirrors, item.t);
                continue;
            }

            // Vertical
            for (int i = item.r+1; i < H; i++) {
                if (grid[i][item.c] == '*') break;
                if (visited[i][item.c] == 1) continue;
                visited[i][item.c] += 1;
                queue.add(new Move(i, item.c, item.t+1));
            }

            for (int i = item.r-1; i >= 0; i--) {
                if (grid[i][item.c] == '*') break;
                if (visited[i][item.c] == 1) continue;
                visited[i][item.c] += 1;
                queue.add(new Move(i, item.c, item.t+1));
            }

            // Horizontal
            for (int i = item.c+1; i < W; i++) {
                if (grid[item.r][i] == '*') break;
                if (visited[item.r][i] == 1) continue;
                visited[item.r][i] += 1;
                queue.add(new Move(item.r, i, item.t+1));
            }

            for (int i = item.c-1; i >= 0; i--) {
                if (grid[item.r][i] == '*') break;
                if (visited[item.r][i] == 1) continue;
                visited[item.r][i] += 1;
                queue.add(new Move(item.r, i, item.t+1));
            }
        }

        System.out.println(mirrors);
    }

    public static class Move {
        int r, c, t;
        public Move(int r, int c, int t) {
            this.r = r; this.c = c; this.t = t;
        }
    }
}
