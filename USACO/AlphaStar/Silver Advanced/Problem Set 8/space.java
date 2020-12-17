import java.util.*;

public class space {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N = Integer.parseInt(input.nextLine());
        char[][] space = new char[N][N];
        int[][] visited = new int[N][N];
        HashSet<List<Integer>> asteroids = new HashSet<List<Integer>>();

        for (int i = 0; i < N; i++) {
            String tmp = input.nextLine();
            for (int j = 0; j < N; j++) {
                space[i][j] = tmp.charAt(j);
                if (space[i][j] == '*') {
                    asteroids.add(Arrays.asList(i, j));
                }
            }
        }

        input.close();
        // System.out.println("Asteroid locations:");
        // System.out.println(asteroids);

        // Use a set to keep track of all the asterisks and then cross off as necessary

        int k = 1;

        while (asteroids.size() > 0) {
            // System.out.println("next asteroid: " + asteroids.iterator().next());
            List<Integer> asteroid = asteroids.iterator().next();
            asteroids.remove(asteroid);
            int i = asteroid.get(0), j = asteroid.get(1);
            if (visited[i][j] != 0 || space[i][j] != '*') {
                asteroids.remove(asteroid);
                continue;
            }

            Queue<Integer[]> queue = new LinkedList<Integer[]>();
            queue.add(new Integer[]{i, j, k});

            while (queue.size() > 0) {
                Integer[] item = queue.remove();
                visited[item[0]][item[1]] = k;

                int[][] moves = {
                    new int[]{1, 0},
                    new int[]{-1, 0},
                    new int[]{0, 1},
                    new int[]{0, -1},
                };

                for (int[] m: moves) {
                    int dr = item[0] + m[0];
                    int dc = item[1] + m[1];
                    if (dr < 0 || dr >= N || dc < 0 || dc >= N) continue;
                    if (visited[dr][dc] != 0) continue;
                    if (space[dr][dc] != '*') continue;
                    queue.add(new Integer[]{dr, dc});
                    asteroids.remove(Arrays.asList(dr, dc));
                }
            }

            k += 1;
        }

        // for (int i = 0; i < N; i++) {
        //     for (int j = 0; j < N; j++) {
        //         if (visited[i][j] != 0) continue;
        //         if (space[i][j] != '*') continue;
        //         Queue<Integer[]> queue = new LinkedList<Integer[]>();
        //         queue.add(new Integer[]{i, j, k});

        //         while (queue.size() > 0) {
        //             Integer[] item = queue.remove();
        //             visited[item[0]][item[1]] = k;

        //             int[][] moves = {
        //                 new int[]{1, 0},
        //                 new int[]{-1, 0},
        //                 new int[]{0, 1},
        //                 new int[]{0, -1},
        //             };

        //             for (int[] m: moves) {
        //                 int dr = item[0] + m[0];
        //                 int dc = item[1] + m[1];
        //                 if (dr < 0 || dr >= N || dc < 0 || dc >= N) continue;
        //                 if (visited[dr][dc] != 0) continue;
        //                 if (space[dr][dc] != '*') continue;
        //                 queue.add(new Integer[]{dr, dc});
        //             }
        //         }

        //         k += 1;
        //     }
        // }


        System.out.println(k-1);
    }
}
