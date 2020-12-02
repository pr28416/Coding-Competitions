import java.util.*;

public class flyingcow {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        N = input.nextInt(); M = N-1;
        input.close();

        visited = new boolean[N+4]; visited[0] = true;

        Queue<Pair> queue = new LinkedList<Pair>();
        queue.add(new Pair(N, 0));
        Pair i;
        
        while (!queue.isEmpty()) {
            i = queue.remove();

            if (i.n < 1) continue;
            else if (i.n == 1) M = Integer.min(i.m, M);
            else if (i.m > M) continue;

            else {
                if (visited[i.n]) continue;
                visited[i.n] = true;

                if (i.n % 3 == 0) queue.add(new Pair(i.n/3, i.m+1));
                if (i.n < N+3) queue.add(new Pair(i.n+1, i.m+1));
                if (i.n > 0) queue.add(new Pair(i.n-1, i.m+1));
            }
        }
        System.out.println(M);
        
    }

    public static class Pair {
        int n, m;
        public Pair(int a, int b) {n = a; m = b;}
    }

    static int N;
    static int M;
    static boolean[] visited;
}