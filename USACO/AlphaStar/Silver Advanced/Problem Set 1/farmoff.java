import java.util.*;
public class farmoff {

    public static long pow(long n, long p, long m) {
        long a = 1;
        for (long i = 0; i < p; i++) {
            a = (a * (n % m)) % m;
        }
        return a;
    }

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        long a = input.nextInt();
        long b = input.nextInt();
        long c = input.nextInt();
        long d = input.nextInt();
        long e = input.nextInt();
        long f = input.nextInt();
        long g = input.nextInt();
        long h = input.nextInt();
        long M = input.nextInt();
        input.close();
        pair[] best = new pair[3*N];
        for (long i = 0; i < 3*N; i++) {
            long w = (a*pow(i, 5, d)+b*pow(i, 2, d)+c) % d;
            long u = (e*pow(i, 5, h)+f*pow(i, 3, h)+g) % h;
            best[(int)i] = new pair(u, w);
        }
        Arrays.sort(best, new comp());
        long sum = 0;
        for (int i = 0; i < N; i++) {
            sum += best[best.length-1-i].w;
        }
        System.out.println(sum%M);
    }
}

class pair {
    long u, w;
    public pair(long u, long w) {
        this.u = u; this.w = w;
    }
    public String toString() {
        return ""+u+" "+w;
    }
}

class comp implements Comparator<pair> {
    public int compare(pair a, pair b) {
        if (a.u == b.u) {
            if (a.w < b.w) return -1;
            else if (a.w == b.w) return 0;
            return 1;
        }
        return a.u < b.u ? -1 : 1;
    }
}