import java.util.Scanner;
public class assign {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        N = input.nextInt(); K = input.nextInt();
        grid = new char[N+1][N+1];

        for (int i = 0; i < K; i++) {
            char c = input.next().charAt(0);
            int a = input.nextInt(), b = input.nextInt();
            grid[a][b] = c; grid[b][a] = c;
        }
        input.close();

        recurse(new int[N+1], 1);
        System.out.println(fin);
    }

    static char[][] grid;
    static int N, K, fin = 0;
    
    public static void recurse(int[] comb, int pos) {
        if (pos == N+1) fin += 1;
        else {
            outer: for (int i = 0; i < 3; i++) {
                for (int j = 0; j < pos; j++) {
                    if (grid[pos][j] == 'S' && comb[j] != i) continue outer;
                    else if (grid[pos][j] == 'D' && comb[j] == i) continue outer;
                }
                comb[pos] = i;
                recurse(comb, pos+1);
                comb[pos] = 0;
            }
        }
    }
}