import java.util.*;
import java.io.*;

public class NoTimeToPaint {
    public static void main(String[] args) throws IOException {
        // BufferedReader input = new BufferedReader(new FileReader(new File("NoTimeToPaint.txt")));
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String[] line = input.readLine().split(" ");
        int N = Integer.parseInt(line[0]), Q = Integer.parseInt(line[1]);
        
        
        String target = "[" + input.readLine();
        // System.out.println(target);
        // int[] prefix = new int[N+1]; prefix[1] = 1;
        // for (int i = 1; i < N; i++) {
        //     if (target.charAt(i) == target.charAt(i-1)) prefix[i+1] = prefix[i];
        //     else prefix[i+1] = prefix[i] + 1;
        // }
        
        // System.out.println(Arrays.toString(prefix));


        
        int[] strokes = new int[N+1];
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        int strokeNum = 1;
        for (int i = 0; i < 25; i++) {
            for (int j = 1; j < N+1; j++) {
                if (target.charAt(j) >= alphabet.charAt(i)) {
                    strokes[j] = strokeNum;
                } else {
                    strokeNum++;
                }
                // if (target.charAt(j) == target.charAt(j-1)) {
                //     strokes[j] = strokes[j-1];
                // } else {
                //     strokeNum++;
                // }
            }
            strokeNum++;
            // System.out.printf("Applying %s: %s\n", alphabet.charAt(i), Arrays.toString(strokes));
        }
        
        // System.out.println("strokes: " + Arrays.toString(strokes));
        
        
        HashSet<Integer> seen = new HashSet<Integer>();
        int[] prefix = new int[N+1];
        
        for (int i = 1; i < N+1; i++) {
            seen.add(strokes[i]);
            // System.out.println(seen);
            prefix[i] = seen.size();
        }
        
        // System.out.println("prefix: " + Arrays.toString(prefix));

        int lo, up;
        for (int q = 0; q < Q; q++) {
            line = input.readLine().split(" ");
            lo = Integer.parseInt(line[0])-1;
            up = Integer.parseInt(line[1]);
            // System.out.println("Don't want " + target.substring(lo, up));
            // System.out.printf("Want %s and %s\n", target.substring(0, lo), target.substring(up, N));
            // // System.out.println(lo + " " + up);
            // System.out.printf("Left substring [%s, %s): %s, right substring [%s, %s): %s - %s = %s\n",
            //     0, lo,
            //     prefix[lo],
            //     up, N,
            //     prefix[N],
            //     prefix[up],
            //     prefix[N]-prefix[up]
            // );

            System.out.println(prefix[lo] + prefix[N] - prefix[up]);
        }

        input.close();
    }
}