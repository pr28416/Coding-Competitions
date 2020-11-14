import java.util.Scanner;
public class maxcross {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt(), K = input.nextInt(), B = input.nextInt();
        int[] signals = new int[N+1];
        for (int i = 1; i < N+1; i++) signals[i] = 1;
        for (int i = 0; i < B; i++) signals[input.nextInt()] = 0;
        input.close();

        int[] sums = new int[N+1];
        for (int i = 1; i < N+1; i++) sums[i] = sums[i-1] + signals[i];

        int finK = N;
        outer: for (int k = 1; k < N; k++) {
            for (int i = 0; i < N+1-K; i++) {
                if (sums[i+K]-sums[i]+k >= K) {finK = k; break outer;}
            }
        }

        System.out.println(finK);
    }
}