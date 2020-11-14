import java.util.*;
public class fairphoto {
    public static class pair implements Comparable<pair> {
        int n; char c;
        public pair(int n, char c) {this.n=n; this.c=c;}
        public String toString() {return n+" "+c;}

        @Override
        public int compareTo(fairphoto.pair o) {
            return this.n - o.n;
        }
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        pair[] cows = new pair[N+1]; cows[0] = new pair(0, '\0');
        for (int i = 1; i < N+1; i++) {
            cows[i] = new pair(input.nextInt(), input.next().charAt(0));
        }
        input.close(); Arrays.sort(cows);

        int maxCount = 0, tmp = 0;

        // Count Gs
        for (int i = 1; i < N+1; i++) {
            if (cows[i].c == 'G') continue;
            else {
                if (cows[i-1].n-cows[tmp].n > maxCount) maxCount = cows[i-1].n-cows[tmp].n;
                tmp = i+1;
            }
        }

        // Count Hs
        tmp = 0;
        for (int i = 1; i < N+1; i++) {
            if (cows[i].c == 'H') continue;
            else {
                if (cows[i-1].n-cows[tmp].n > maxCount) maxCount = cows[i-1].n-cows[tmp].n;
                tmp = i+1;
            }
        }

        // Count G-Hs
        int[] sums = new int[N+1];
        for (int i = 1; i < N+1; i++) {
            sums[i] = sums[i-1] + (cows[i].c=='G'?1:-1);
        }

        Integer[] start = new Integer[2*N+1], end = new Integer[2*N+1];
        for (int i = 0; i < N+1; i++) {
            if (start[sums[i]+N] == null) {
                start[sums[i]+N] = i;
                end[sums[i]+N] = i;
            } else {
                end[sums[i]+N] = i;
            }
        }

        for (int i = 0; i < 2*N+1; i++) {
            if (start[i] == null || start[i] == end[i] || start[i] >= cows.length-1) continue;
            if (cows[end[i]].n-cows[start[i]+1].n > maxCount) {
                maxCount = cows[end[i]].n-cows[start[i]+1].n;
            }
        }

        System.out.println(maxCount);
    }
}