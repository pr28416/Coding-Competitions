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

        // for (Collection<Integer> i: adjList) System.out.println(i);
        // for (int i: numCows) System.out.println(i);

        int[] visited = new int[N];
        visited[0] = 1;
        // while (cap < N-1) {
        //     cap *= 2;
        //     c++;
        // }
        int fin = 0;
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(0);
        while (!queue.isEmpty()) {
            int item = queue.remove();

            // Duplicate enough cows to cover adjacent
            while (visited[item] < adjList.get(item).size()) {
                visited[item] *= 2;
                fin += 1;
            }
            // Spread a cow each day
            for (int n: adjList.get(item)) {
                if (visited[n] != 0) continue;
                visited[n] = 1;
                fin += 1;
                queue.add(n);
                // adjList.get(n).remove(item);
            }
        }

        //     for (int n: adjList.get(item)) {
        //         if (visited[n] == 0) {
        //             visited[n] = (item == 0 ? 0 : visited[item])+1;
        //             queue.add(n);
        //         }
        //     }
        // }
        // int sum = c;
        // for (int i = 1; i < N; i++) {
        //     sum += visited[i];
        // }
        // // System.out.println(Arrays.toString(visited));
        // System.out.println(sum);
        System.out.println(fin);
    }
}
