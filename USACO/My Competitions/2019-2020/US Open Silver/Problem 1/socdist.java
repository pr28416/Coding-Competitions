import java.io.*;

class socdist {

    // N = # cows
    // M = # intervals

    static int N;
    static int M;
    static long[][] intervals;

    public static long[][] split(long[][] x) {
        if (x.length == 1) {
            return x;
        }

        long[][] a = new long[x.length/2][2];
        for (int i = 0; i < x.length/2; i++) {
            a[i] = x[i];
        }
        long[][] b = new long[x.length-x.length/2][2];
        for (int i = x.length/2; i < x.length; i++) {
            b[i-x.length/2] = x[i];
        }
        a = split(a);
        b = split(b);
        return merge(a, b);
    }

    public static long[][] merge(long[][] a, long[][] b) {
        long[][] x = new long[a.length+b.length][2];
        int aCount = 0, bCount = 0, xIdx = 0;
        while (aCount < a.length && bCount < b.length) {
            if (a[aCount][0] < b[bCount][0]) {
                x[xIdx++] = a[aCount++];
            } else {
                x[xIdx++] = b[bCount++];
            }
        }
        while (aCount < a.length) x[xIdx++] = a[aCount++];
        while (bCount < b.length) x[xIdx++] = b[bCount++];
        return x;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File("socdist.in")));
        PrintWriter writer = new PrintWriter(new File("socdist.out"));

        String[] t = reader.readLine().split(" ");
        N = Integer.parseInt(t[0]);
        M = Integer.parseInt(t[1]);
        intervals = new long[M][2];
        for (int i = 0; i < M; i++) {
            t = reader.readLine().split(" ");
            intervals[i][0] = Long.parseLong(t[0]);
            intervals[i][1] = Long.parseLong(t[1]);
        }

        intervals = split(intervals);
        
        // for (long[] a: intervals) {
        //     for (long b: a) {
        //         System.out.print(b+" ");
        //     }
        //     System.out.println();
        // }

        long answer = 1;

        loop1:
        for (long D = (intervals[M-1][1]+1) / N+1; D > 1; D--) {
            // Start at end interval
            int num_interval = M-1;
            int num_cows_left = N;
            long pos = intervals[num_interval][1];

            loop2:
            while (num_cows_left > 0 && num_interval >= 0 && pos >= 0) {
                // Place the cow
                num_cows_left--;
                if (num_cows_left == 0) break;

                // Determine next location

                // If a position can be found in the same range
                if (pos - D >= intervals[num_interval][0]) {
                    pos -= D;
                    continue;
                } else {
                    // Else while a position can be found in the previous range
                    while (num_interval >= 0) {
                        num_interval --;
                        if (num_interval < 0) break;

                        // If next pos falls in between
                        if (pos - D >= intervals[num_interval][0] && pos - D <= intervals[num_interval][1]) {
                            pos -= D;
                            continue loop2;
                        }
                        // Else if next pos greater than interval upper bound
                        else if (pos - D >= intervals[num_interval][1]) {
                            pos = intervals[num_interval][1];
                            continue loop2;
                        }
                    }

                    if (num_interval < 0) continue loop1;
                }
            }

            if (num_cows_left == 0) {
                answer = D;
                break;
            }
        }

        // System.out.println("Answer: "+answer);
        reader.close();

        writer.println(answer);
        writer.close();
    }



}