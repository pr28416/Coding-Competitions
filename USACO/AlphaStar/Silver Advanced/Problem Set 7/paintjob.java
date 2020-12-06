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
        Set<Integer> seen = new HashSet<Integer>();
        queue.add(new tuple(A, 0));

        int j = 0;

        while (queue.size() > 0) {
            if (j > Integer.MAX_VALUE/2) {
                System.out.println(-1);
                break;
            }
            boolean notSeen = true;

            tuple item = queue.remove();
            if (item.a == B) {
                System.out.println(item.b);
                break;
            }

            for (int i = 0; i < colors.length; i++) {
                int n = item.a * colors[i] % P;
                // if (!seen.contains(n)) {
                    // seen.add(n);
                    notSeen = false;
                    queue.add(new tuple(n, item.b+1));
                // }
            }

            if (notSeen) {
                System.out.println(-1);
                break;
            }

            j += 1;
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
