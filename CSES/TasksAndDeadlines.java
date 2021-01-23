import java.util.*;
import java.io.*;

public class TasksAndDeadlines {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        int[][] intervals = new int[N][2];
        String[] line;
        for (int i = 0; i < N; i++) {
            line = input.readLine().split(" ");
            intervals[i][0] = Integer.parseInt(line[0]);
            intervals[i][1] = Integer.parseInt(line[1]);
        }
        input.close();
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] != o2[0]) return o1[0] - o2[0];
                else return o1[1] - o2[1];
            }
        });
        
        long reward = 0;
        long time = 0;
        for (int[] i: intervals) {
            time += (long)i[0];
            reward += (long)i[1] - (long)time;
        }
        System.out.println(reward);
    }
}