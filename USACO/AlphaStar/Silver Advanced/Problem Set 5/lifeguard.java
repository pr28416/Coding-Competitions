import java.util.*;

public class lifeguard {
    public static void main(String[] args) {
        // Get input
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int[][] intervals = new int[2*N][3];
        for (int i = 0; i < N; i++) {
            intervals[i][0] = input.nextInt();
            intervals[i][1] = i;
            intervals[i][2] = 1;
            intervals[i+N][0] = input.nextInt();
            intervals[i+N][1] = i;
            intervals[i+N][2] = -1;
        }
        input.close();
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return o1[0]-o2[0];
            }
        });

        // Compute cow alone times
        int[] cowsAlone = new int[N];
        HashSet<Integer> workingCows = new HashSet<Integer>();
        int prevTime = 0;
        int workingTime = 0;

        for (int i = 0; i < intervals.length; i++) {
            // Check if cow is working alone
            if (workingCows.size() == 1) {
                cowsAlone[workingCows.iterator().next()] += intervals[i][0]-prevTime;
            }
            // Increment time being worked
            if (workingCows.size() != 0) {
                workingTime += intervals[i][0]-prevTime;
            }
            // Add/remove cow
            if (intervals[i][2] == 1) {
                workingCows.add(intervals[i][1]);
            } else {
                workingCows.remove(intervals[i][1]);
            }
            prevTime = intervals[i][0];
        }
        
        // Calculate largest remaining time when removing each cow
        int remaining = 0;
        for (int i: cowsAlone) {
            remaining = Integer.max(remaining, workingTime - i);
        }

        System.out.println(remaining);
    }
}