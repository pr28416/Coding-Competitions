import java.util.*;
import java.io.*;
public class lifeguards {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new File("lifeguards.in"));
        int N = input.nextInt();
        Tuple[] intervals = new Tuple[2*N];
        int[] individuals = new int[N];
        for (int i = 0; i < 2*N; i += 2) {
            intervals[i] = new Tuple(input.nextInt(), 1, i/2);
            intervals[i+1] = new Tuple(input.nextInt(), -1, (i+1)/2);
        }
        input.close();
        Arrays.sort(intervals, new Comparator<Tuple>() {
            @Override
            public int compare(lifeguards.Tuple o1, lifeguards.Tuple o2) {
                return o1.time - o2.time;
            }
        });

        HashSet<Integer> set = new HashSet<Integer>();
        int totalWorkTime = 0;
        int prevTime = 0;
        for (Tuple i: intervals) {
            if (i.toggle == -1 && set.size() == 1) {
                individuals[i.id] += i.time - prevTime;
            } else if (i.toggle == 1 && set.size() == 1) {
                individuals[set.iterator().next()] += i.time - prevTime;
            }
            if (i.toggle == 1) {
                set.add(i.id);
                if (set.size() != 1) {
                    totalWorkTime += i.time - prevTime;
                }
            } else {
                set.remove(i.id);
                totalWorkTime += i.time - prevTime;
            }
            prevTime = i.time;
        }
        int res = Integer.MAX_VALUE;
        for (int i: individuals) res = Integer.min(i, res);
        PrintWriter writer = new PrintWriter(new File("lifeguards.out"));
        writer.println(totalWorkTime-res);
        writer.close();
    }

    public static class Tuple {
        int time, toggle, id;
        public Tuple(int time, int toggle, int id) {
            this.time = time;
            this.toggle = toggle;
            this.id = id;
        }
        public String toString() {
            return String.format("T:%s, o:%s, i:%s", time, toggle, id);
        }
    }
}
