import java.util.*;

public class flyingcow {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        N = input.nextInt(); M = N-1;
        input.close();

        visited = new boolean[N+1]; visited[0] = true;

        goHome(N, 0);
        System.out.println(M);
        // 1 2 3 4 5
    }

    static int N;
    static int M;
    static boolean[] visited;

    public static void goHome(int pos, int m) {
        for (int i = 0; i < m; i++) System.out.print("  ");
        System.out.println(pos);
        if (pos < 1) return;
        else if (pos == 1) {
            if (m < M) M = m;
        }
        else if (m > N) return;
        else {
            if (visited[pos]) return;
            visited[pos] = true;
            // Case 1: Use the Flying cow
            if (pos % 3 == 0) goHome(pos/3, m+1);
            // else {
            // Case 2: Drag left
            if (pos > 0) goHome(pos-1, m+1);
            // Case 3: Drag right
            if (pos < N) goHome(pos+1, m+1);
            // }
        }
    }
}