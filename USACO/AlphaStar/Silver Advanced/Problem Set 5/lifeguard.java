import java.util.*;

public class lifeguard {
    public static void main(String[] args) {
        // Get input
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        int[][] intervals = new int[2*N][3];
        TreeMap<Integer, Integer> cowsAlone = new TreeMap<Integer, Integer>();
        for (int i = 0; i < N; i++) {
            intervals[i][0] = input.nextInt();
            intervals[i][1] = i;
            intervals[i][2] = 1;
            // cowsAlone.put(intervals[i][1], new int[2]);
            intervals[i+N][0] = input.nextInt();
            intervals[i+N][1] = i;
            intervals[i+N][2] = -1;
            // cowsAlone.put(intervals[i+N][1], new int[2]);
        }
        input.close();
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] o1, int[] o2) {
                return o1[0]-o2[0];
            }
        });
        // for (int[] i: intervals) System.out.println(Arrays.toString(i));

        HashSet<Integer> workingCows = new HashSet<Integer>();
        int activeCount = 0;
        int totalTime = 0;
        int tempStart = 0;
        int smallest = Integer.MAX_VALUE;
        for (int i = 0; i < 2*N; i++) {
            int prevActive = activeCount;
            activeCount += intervals[i][2];
            
            if (prevActive == 0 && activeCount == 1) { // Start
                cowsAlone.put(intervals[i][1], intervals[i][0]);
                // cowsAlone.get(intervals[i][1]) = intervals[i][0];
                tempStart = intervals[i][1];
            } else if (prevActive == 1 && activeCount == 2) { // Stop
                // cowsAlone.get(workingCows.iterator().next())[1] = intervals[i][0];
                int val = workingCows.iterator().next();
                // cowsAlone.put(val, intervals[i][0]-cowsAlone.get(val));
                if (smallest > intervals[i][0]-cowsAlone.get(val)) {
                    smallest = intervals[i][0]-cowsAlone.get(val);
                }
                cowsAlone.remove(val);
            }
            
            if (intervals[i][2] == 1) {
                workingCows.add(intervals[i][1]);
            } else {
                workingCows.remove(intervals[i][1]);
            }
            
            if (prevActive == 2 && activeCount == 1) { // Start
                // cowsAlone.get()[0] = intervals[i][0];
                cowsAlone.put(workingCows.iterator().next(), intervals[i][0]);
            } else if (prevActive == 1 && activeCount == 0) { // Stop
                // cowsAlone.get(intervals[i][1])[1] = intervals[i][0];
                // cowsAlone.put(intervals[i][1], intervals[i][0]-cowsAlone.get(intervals[i][1]));
                if (smallest > intervals[i][0]-cowsAlone.get(intervals[i][1])) {
                    smallest = intervals[i][0]-cowsAlone.get(intervals[i][1]);
                }
                cowsAlone.remove(intervals[i][1]);
                totalTime += intervals[i][0] - tempStart;
            }
        }

        // for (Map.Entry<Integer, Integer> entry: cowsAlone.entrySet()) {
        //     System.out.printf("%s: %s\n", entry.getKey(), entry.getValue());
        // }

        // System.out.println("Total time spent working: " + totalTime);
        System.out.println(totalTime - (smallest > totalTime ? totalTime : smallest));
    }
}

/*

1:  1 4
2:  3 6
3:  3 7
4:  3 8
5:  5 9

1       4                   1 is alone from 1 to 3 --> 2
      3       6             2 is never alone --> 0
      3         7           3 is never alone --> 0
      3           8         4 is never alone --> 0
           5        9       5 is alone from 8 to 9 --> 1

put alone times into treemap


1 4
3 7
5 9
*/