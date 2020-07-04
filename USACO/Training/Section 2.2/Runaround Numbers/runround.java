/*
ID: pranav.19
LANG: JAVA
TASK: runround
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;

class runround {
    public static void main(String[] args) throws IOException {
        long M = 0;
        BufferedReader f = new BufferedReader(new FileReader("runround.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("runround.out")));
        
        M = Long.parseLong(f.readLine())+1;
        f.close();
        
        while (!isRunaround(M)) {
            M++;
        }
        // System.out.println(M);
        out.println(M);
        out.close();
    }

    public static boolean isRunaround(long m) {

        int[] n = new int[(""+m).length()];
        int i = n.length-1;
        while (m > 0) {
            n[i] = (int)(m % 10);
            if (n[i] == 0) {
                return false;
            }
            m /= 10;
            i--;
        }

        int[] a = n.clone();
        Arrays.sort(a);
        for (int k = 0; k < a.length-1; k++) {
            if (a[k] == a[k+1]) {
                return false;
            }
        }

        int[] used = new int[n.length];
        used[0] = 1;
        int cur = 0;
        int oneCount = 1;
        while (true) {
            cur = (cur + n[cur]) % n.length;
            if (oneCount == n.length && cur == 0) {
                return true;
            }
            if (used[cur] >= 1) {
                return false;
            }
            used[cur] = 1;
            oneCount++;
        }
        // return true;
    }
}