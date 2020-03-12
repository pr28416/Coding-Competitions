/*
ID: pranav.19
LANG: JAVA
TASK: nocows
*/

import java.io.*;
import java.util.*;

class nocows {

    // 3 <= N < 200
    // 1 < K < 100
    static int N, K;
    static int[] tree;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File("nocows.in")));
        String[] c = reader.readLine().split(" ");
        N = Integer.parseInt(c[0]);
        K = Integer.parseInt(c[1]);

        // Set up tree array to have 2^k items - need to change later because 2^100 is too big
        tree = new int[(int)Math.pow(2, K)];
    }

}