import java.util.*;

public class pathfind {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int N = input.nextInt(), M = input.nextInt()-1;
        int[][] grid = new int[N][N];
        int[] visited = new int[N];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                grid[i][j] = input.nextInt();
            }
        }

        input.close();

        Queue<Pair> queue = new LinkedList<Pair>();
        queue.add(new Pair(M, 0));
        int prevLvl = 0;
        TreeSet<Integer> set = new TreeSet<Integer>();

        while (queue.size() > 0) {
            Pair item = queue.remove();

            if (item.b != prevLvl) {
                prevLvl = item.b;
                StringBuilder string = new StringBuilder();
                for (int i: set) {
                    string.append(i+1+" ");
                }
                string.deleteCharAt(string.length()-1);
                System.out.println(string);
                set.clear();
            }

            set.add(item.a);
            visited[item.a] = 1;

            for (int i = 0; i < visited.length; i++) {
                if (i == item.a) continue;
                if (visited[i] == 0 && grid[item.a][i] == 1) {
                    queue.add(new Pair(i, item.b+1));
                    visited[i] = 1;
                }
            }
        }

        StringBuilder string = new StringBuilder();
        for (int i: set) {
            string.append(i+1+" ");
        }
        string.deleteCharAt(string.length()-1);
        System.out.println(string);

    }

    public static class Pair {
        int a, b;
        public Pair(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }
}
