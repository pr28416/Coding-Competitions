import java.util.*;

public class paintjob {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int A = input.nextInt(), B = input.nextInt();
        int N = input.nextInt(), P = input.nextInt();

        int[] colors = new int[N];
        for (int i = 0; i < N; i++) {
            colors[i] = input.nextInt();
        }

        input.close();

        Queue<tuple> queue = new LinkedList<tuple>();
        int[] visited = new int[P];
        visited[A % P] = 1;
        int totalP = 1;
        queue.add(new tuple(A, 0));

        while (queue.size() > 0) {
            tuple item = queue.remove();

            if (item.a == B) {
                System.out.println(item.b);
                break;
            }
            
            if (totalP > P) {
                System.out.println(-1);
                break;
            }
            
            for (int i = 0; i < colors.length; i++) {
                int n = item.a * colors[i] % P;
                if (visited[n] == 0) {
                    visited[n] = 1;
                    totalP += 1;
                    queue.add(new tuple(n, item.b+1));
                }
            }
        }
    }

    public static class tuple {
        int a, b;
        public tuple(int a, int b) {
            this.a = a;
            this.b = b;
        }
    }
}
