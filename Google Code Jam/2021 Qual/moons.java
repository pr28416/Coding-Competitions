import java.util.*;

public class moons {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        for (int t = 1; t <= T; t++) {
            int cost = solve(input.nextInt(), input.nextInt(), input.next().toCharArray());
            System.out.printf("Case #%s: %s\n", t, cost);
        }
        input.close();
    }

    public static int solve(int x, int y, char[] c) {
        int cost = 0;
        // System.out.println(x);
        // System.out.println(y);
        // System.out.println(Arrays.toString(c));
        for (int i = 0; i < c.length; i++) {
            // System.out.printf("i=%s: c=%s\n", i, Arrays.toString(c));
            // Expand right
            for (int j = i+1; j < c.length; j++) {
                if (c[j] != '?') break;
                c[j] = c[i];
            }
            // Expand left
            for (int j = i-1; j >= 0; j--) {
                if (c[j] != '?') break;
                c[j] = c[i];
            }
            // System.out.printf("\t-->%s\n", Arrays.toString(c));
        }
        for (int i = 0; i < c.length-1; i++) {
            if (c[i] == 'C' && c[i+1] == 'J') cost += x;
            else if (c[i] == 'J' && c[i+1] == 'C') cost += y;
        }
        return cost;
    }
}

/*
C_C --> C
C_J --> C or J, no matter what you will have both fines
J_C --> C or J, no matter what you will have both fines
J_J --> J

CJ_CC_
------
CJCCCC --> CJ JC --> x + y
CJCCCJ --> CJ JC CJ --> 2x + y
CJJCCC --> CJ JC --> x + y
CJJCCJ --> CJ JC CJ --> 2x + y


*/