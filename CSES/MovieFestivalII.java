import java.util.*;
import java.io.*;

public class MovieFestivalII {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] line = input.readLine().split(" ");
        int N = Integer.parseInt(line[0]), K = Integer.parseInt(line[1]);
        int[][] intervals = new int[N][2];
        for (int i = 0; i < N; i++) {
            line = input.readLine().split(" ");
            intervals[i][0] = Integer.parseInt(line[0]);
            intervals[i][1] = Integer.parseInt(line[1]);
        }
        input.close();
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[1] != o2[1]) return o1[1]-o2[1];
                else return o1[0]-o2[0];
            }
        });

        for (int[] i: intervals) System.out.println(Arrays.toString(i));
        // int[][] timestamps = new int[2*N][2];

        Queue<Integer> workers = new ArrayDeque<Integer>();
        int inactive = K;
        int count = 0;

        for (int[] interval: intervals) {
            while (!workers.isEmpty() && workers.peek() <= interval[0]) {
                inactive++;
                workers.remove();
            }
            if (inactive > 0) {
                count++;
                inactive--;
                workers.add(interval[1]);
            }
        }
        
        System.out.println(count);

        // for (int i = 0; i < N; i++) {
            // timestamps[2*i][0] = intervals[i][0];
            // timestamps[2*i+1][0] = intervals[i][1];
        // }
        // Arrays.sort(timestamps);
        // System.out.println(Arrays.toString(timestamps));
    }
}

/*
10, 2
[40, 44] - y [44]
[37, 74] - y [44, 74]
[70, 81] - y [74, 81]
[62, 83] - /
[11, 85] - /
[17, 86] - /
[38, 87] - /
[92, 95] - y []
[65, 97]
[99, 100]
*/