import java.util.*;

public class cowntagion {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<HashSet<Integer>> adjList = new ArrayList<HashSet<Integer>>();
        
        int N = input.nextInt();
        int[] numCows = new int[N];

        for (int i = 0; i < N; i++) {
            adjList.add(new HashSet<Integer>());
            // numCows[i] = 1;
        }

        numCows[0] = 1;

        for (int i = 0; i < N-1; i++) {
            int k = input.nextInt()-1, j = input.nextInt()-1;
            adjList.get(k).add(j);
            adjList.get(j).add(k);
        }

        input.close();

        int[] visited = new int[N];
        visited[0] = 1;

        int fin = 0;
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(0);
        while (!queue.isEmpty()) {
            int item = queue.remove();

            // Duplicate enough cows to cover adjacent
            while (visited[item]-1 < adjList.get(item).size()) {
                visited[item] *= 2;
                fin += 1;
            }
            // Spread a cow each day
            for (int n: adjList.get(item)) {
                if (visited[n] != 0) continue;
                visited[n] = 1;
                fin += 1;
                queue.add(n);
                adjList.get(n).remove(item);
            }
        }

        System.out.println(fin);
    }
}
