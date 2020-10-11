import java.util.Scanner;
import java.util.Arrays;

public class bcount {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int Q = input.nextInt();
        int[] cowBreeds = new int[N];
        for (int i = 0; i < N; i++) {
            cowBreeds[i] = input.nextInt();
        }
        int[][] queries = new int[Q][2];
        for (int i = 0; i < Q; i++) {
            queries[i][0] = input.nextInt();
            queries[i][1] = input.nextInt();
        }
        input.close();
        int[] prev = {1, N};
        int[] breedCount = new int[3];
        int[][] answers = new int[Q][3];
        int a = 0;
        for (int i: cowBreeds) {
            breedCount[i-1] += 1;
        }
        for (int[] query: queries) {
            // Modify lower bound
            if (prev[0] < query[0]) {
                for (int i = prev[0]-1; i < query[0]-1; i++) {
                    breedCount[cowBreeds[i]-1] -= 1;
                }
            } else {
                for (int i = prev[0]-2; i > query[0]-2; i--) {
                    breedCount[cowBreeds[i]-1] += 1;
                }
            }
            // Modify upper bound
            if (prev[1] < query[1]) {
                for (int i = prev[1]; i < query[1]; i++) {
                    breedCount[cowBreeds[i]-1] += 1;
                }
            } else {
                for (int i = prev[1]-1; i > query[1]-1; i--) {
                    breedCount[cowBreeds[i]-1] -= 1;
                }
            }
            answers[a++] = new int[]{breedCount[0], breedCount[1], breedCount[2]};
            prev = query;
        }
        for (int[] i: answers) {
            System.out.printf("%s %s %s\n", i[0], i[1], i[2]);
        }
    }
}
