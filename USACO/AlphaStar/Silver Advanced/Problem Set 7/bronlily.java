import java.util.*;

public class bronlily {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int M = input.nextInt();
        int N = input.nextInt();
        int M1 = input.nextInt();
        int M2 = input.nextInt();

        int[][] pond = new int[M][N];
        boolean[][] visited = new boolean[M][N];
        
        Coord start = new Coord(0, 0, 0);
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                pond[i][j] = input.nextInt();
                if (pond[i][j] == 3) {
                    start = new Coord(i, j, 0);
                }
            }
        }
        
        input.close();
        
        Queue<Coord> queue = new LinkedList<Coord>();
        queue.add(start);

        while (queue.size() > 0) {
            Coord item = queue.remove();

            if (pond[item.a][item.b] == 4) {
                System.out.println(item.c);
                break;
            }
            visited[item.a][item.b] = true;

            int[][] moves = {
                new int[]{M1, M2},
                new int[]{-M1, M2},
                new int[]{M1, -M2},
                new int[]{-M1, -M2},
                new int[]{M2, M1},
                new int[]{-M2, M1},
                new int[]{M2, -M1},
                new int[]{-M2, -M1},
            };

            for (int i = 0; i < moves.length; i++) {
                int dr = item.a + moves[i][0];
                int dc = item.b + moves[i][1];
                if (dr < 0 || dr >= M || dc < 0 || dc >= N) continue;
                if (visited[dr][dc] || pond[dr][dc] != 1 && pond[dr][dc] != 4) continue;
                visited[dr][dc] = true;
                queue.add(new Coord(dr, dc, item.c+1));
            }
        }
    }

    public static class Coord {
        int a, b, c;
        public Coord(int a, int b, int c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }
    }
}
