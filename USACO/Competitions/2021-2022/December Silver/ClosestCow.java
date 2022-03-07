import java.util.*;
import java.io.*;

public class ClosestCow {

    public static int bounded_search(int x, int[] lst, boolean lo_bound) {
        int lo = 0, up = lst.length, mid;
        while (lo < up) {
            mid = (lo+up)/2;
            if (lo_bound) {
                if (x <= lst[mid]) up = mid;
                else lo = mid + 1;
            } else {
                if (x < lst[mid]) up = mid;
                else lo = mid + 1;
            }
        }
        return lo_bound ? lo-1 : lo;
    }

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
//        Scanner input = new Scanner(new File("/Users/pranavramesh/Developer/Coding-Competitions/USACO/Competitions/2021-2022/December Silver/p1_0.txt"));
        int K = input.nextInt(), M = input.nextInt(), N = input.nextInt();
        int[][] patches = new int[K][2];
        for (int i = 0; i < K; i++) patches[i] = new int[]{input.nextInt(), input.nextInt()};
        int[] nhoj = new int[M + 2];
        for (int i = 1; i <= M; i++) nhoj[i] = input.nextInt();
        nhoj[M + 1] = Integer.MAX_VALUE;
        nhoj[0] = Integer.MIN_VALUE + 10;
        input.close();
        Arrays.sort(nhoj);

//        for (int[] i: patches) {
//            System.out.println(Arrays.toString(i));
//        }
//        for (int i: nhoj) {
//            System.out.println(i);
//        }

//        LinkedList<Integer[]> intervals = new LinkedList<Integer[]>();
        Node intervals = new Node();
        Node trav = intervals;
        for (int i = 0; i < K; i++) {
            int lo = nhoj[bounded_search(patches[i][0], nhoj, true)];
            int up = nhoj[bounded_search(patches[i][0], nhoj, false)];
//            System.out.printf("%s %s %s\n", patches[i][0], lo, up);
            if (up - patches[i][0] <= patches[i][0] - lo) lo = 2 * patches[i][0] - up;
            else up = 2 * patches[i][0] - lo;
//            intervals.add(new Integer[]{lo, up, patches[i][1]});
            trav.intervals = new long[]{lo, up, patches[i][1]};
            trav.next = new Node();
            trav.next.prev = trav;
            trav = trav.next;
        }
        trav.prev.next = null;
//        for (Integer[] i: intervals) {
//            System.out.println(Arrays.toString(i));
//        }
//        trav = intervals;
//        do {
//            System.out.println(Arrays.toString(trav.intervals));
//            trav = trav.next;
//        } while (trav != null);

        trav = intervals;
        while (trav != null) {
//            System.out.println("Currently on: " + Arrays.toString(trav.intervals));
            if (trav.prev == null) {
                if (trav.intervals[1] > trav.next.intervals[0]) {
                    trav.intervals[0] = Long.max(trav.intervals[0], trav.next.intervals[0]);
                    trav.intervals[1] = Long.min(trav.intervals[1], trav.next.intervals[1]);
                    trav.intervals[2] = trav.intervals[2] + trav.next.intervals[2];
                    trav.next = trav.next.next;
                } else {
                    trav = trav.next;
                }
            } else if (trav.next == null) {
                if (trav.prev.intervals[1] > trav.intervals[0]) {
                    trav.prev.intervals[0] = Long.max(trav.intervals[0], trav.prev.intervals[0]);
                    trav.prev.intervals[1] = Long.min(trav.intervals[1], trav.prev.intervals[1]);
                    trav.prev.intervals[2] = trav.intervals[2] + trav.prev.intervals[2];
                    trav.prev.next = trav.next;
                } else {
                    trav = trav.next;
                }
            } else {
                long rightTotal = trav.intervals[2], leftTotal = trav.intervals[2];
                boolean didChange = false;
                if (trav.intervals[1] > trav.next.intervals[0]) {
                    rightTotal += trav.next.intervals[2];
                    didChange = true;
                }
                if (trav.prev.intervals[1] > trav.intervals[0]) {
                    leftTotal += trav.prev.intervals[2];
                    didChange = true;
                }
                if (!didChange) {
                    trav = trav.next;
                    continue;
                }
                if (leftTotal >= rightTotal) {
                    trav.prev.intervals[0] = Long.max(trav.intervals[0], trav.prev.intervals[0]);
                    trav.prev.intervals[1] = Long.min(trav.intervals[1], trav.prev.intervals[1]);
                    trav.prev.intervals[2] = leftTotal;
                    trav.prev.next = trav.next;
                } else {
                    trav.intervals[0] = Long.max(trav.intervals[0], trav.next.intervals[0]);
                    trav.intervals[1] = Long.min(trav.intervals[1], trav.next.intervals[1]);
                    trav.intervals[2] = rightTotal;
                    trav.next = trav.next.next;
                }
            }
        }
//        System.out.println("Done");
        trav = intervals;
        PriorityQueue<Long> queue = new PriorityQueue<Long>();
        while (trav != null) {
            queue.add(-trav.intervals[2]);
//            System.out.println(Arrays.toString(trav.intervals));
            trav = trav.next;
        }
        long total = 0;
        for (int i = 0; i < N; i++) {
            total += queue.remove();
        }
        System.out.println(-total);
    }

    static class Node {
        long[] intervals;
        Node next, prev;
        public Node() {
            intervals = new long[3];
        }
    }
}