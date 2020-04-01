import java.util.*;
import java.io.*;

class moop {

    static int N;
    static int[][] spins;

    public static int[][] split(int[][] x) {
        if (x.length == 1) {
            return x;
        }

        int[][] a = new int[x.length/2][2];
        for (int i = 0; i < x.length/2; i++) {
            a[i] = x[i];
        }
        int[][] b = new int[x.length-x.length/2][2];
        for (int i = x.length/2; i < x.length; i++) {
            b[i-x.length/2] = x[i];
        }
        a = split(a);
        b = split(b);
        return merge(a, b);
    }

    public static int[][] merge(int[][] a, int[][] b) {
        int[][] x = new int[a.length+b.length][2];
        int aCount = 0, bCount = 0, xIdx = 0;
        while (aCount < a.length && bCount < b.length) {
            if (a[aCount][0] < b[bCount][0]) {
                x[xIdx++] = a[aCount++];
            } else if (a[aCount][0] == b[bCount][0]) {
                if (a[aCount][1] < b[bCount][1]) {
                    x[xIdx++] = a[aCount++];
                } else {
                    x[xIdx++] = b[bCount++];
                }
            } else {
                x[xIdx++] = b[bCount++];
            }
        }
        while (aCount < a.length) x[xIdx++] = a[aCount++];
        while (bCount < b.length) x[xIdx++] = b[bCount++];
        return x;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File("moop.in")));
        PrintWriter writer = new PrintWriter(new File("moop.out"));

        N = Integer.parseInt(reader.readLine());
        spins = new int[N][2];
        String[] t;
        for (int i = 0; i < N; i++) {
            t = reader.readLine().split(" ");
            spins[i][0] = Integer.parseInt(t[0]);
            spins[i][1] = Integer.parseInt(t[1]);
        }
        ArrayList<int[]> all = new ArrayList<>();
        spins = split(spins);
        for (int[] i: spins) {
            all.add(i);
            for (int j: i) {
                System.out.print(j+" ");
            }
            System.out.println();
        }

        boolean didChange = true;
        

        while (didChange) {
            didChange = false;
            
            ArrayList<int[]> temp = new ArrayList<>();
            for (int i = 0; i < all.size()-1; i+=2) {
                if (all.get(i)[0] <= all.get(i+1)[0] && all.get(i)[1] <= all.get(i+1)[1]) {
                    temp.add(all.get(i));
                    didChange = true;
                } else if (all.get(i)[0] >= all.get(i+1)[0] && all.get(i)[1] >= all.get(i+1)[1]) {
                    temp.add(all.get(i+1));
                } else {
                    i -= 1;
                }
            }
            all = temp;
        }

        for (int[] i: all) {
            for (int j: i) {
                System.out.print(j+" ");
            }
            System.out.println();
        }

        reader.close();
        writer.close();
    }
}