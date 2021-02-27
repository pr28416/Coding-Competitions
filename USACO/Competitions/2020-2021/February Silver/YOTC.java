import java.util.*;

public class YOTC {

    static boolean debug = false;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt(), K = input.nextInt();
        Integer[] years = new Integer[N];
        for (int i = 0; i < N; i++) {
            years[i] = input.nextInt();
        }
        input.close();
        Arrays.sort(years, Collections.reverseOrder());
        if (debug) System.out.println(Arrays.toString(years));

        // for (int i = 1; i < 20; i++) {
        //     System.out.println(maxjump(i));
        // }
        // System.out.println(maxJump(34, 16));
        // System.out.println(maxJump(34, 25));
        // System.out.println(maxJump(34, 23));
        // System.out.println(upper(5));

        ArrayList<int[]> intervals = maxJump(years);

        int time = 0;
        int i;
        for (i = 0; i < K-1 && i < intervals.size(); i++) {
            time += intervals.get(i)[0]-intervals.get(i)[1];
        }
        if (i < intervals.size()) {
            time += intervals.get(i)[0];
        }
        System.out.println(time);
    }

    // static int maxJump(int m, int n) {
    //     int up = 12*(int)(Math.ceil(m/12.0));
    //     int mid1 = 12*(int)(Math.floor(m/12.0));
    //     int mid2 = 12*(int)(Math.ceil(n/12.0));
    //     int lo = 12*(int)(Math.floor(n/12.0));

    //     if (up == mid2 && mid1 == lo || mid1 == mid2) return up-lo;
    //     else return up-mid1+mid2-lo;
    // }

    static ArrayList<int[]> maxJump(Integer[] years) {
        ArrayList<int[]> intervals = new ArrayList<int[]>();
        for (int i = 0; i < years.length; i++) {
            int u = upper(years[i]);
            int l = lower(years[i]);
            if (intervals.isEmpty()) intervals.add(new int[]{u, l});
            else {
                if (intervals.get(intervals.size()-1)[0] == u) {
                    continue;
                } else if (intervals.get(intervals.size()-1)[1] < u) {
                    continue;
                } else if (intervals.get(intervals.size()-1)[1] == u) {
                    intervals.get(intervals.size()-1)[1] = l;
                } else {
                    intervals.add(new int[]{u, l});
                }
            }
        }
        if (debug) {
            for (int[] i: intervals) {
                System.out.println(Arrays.toString(i));
            }
        }
        return intervals;
    }

    static int upper(int n) {return 12*(int)Math.ceil(n/12.0);}
    static int lower(int n) {return 12*(int)Math.floor(n/12.0);}
}
