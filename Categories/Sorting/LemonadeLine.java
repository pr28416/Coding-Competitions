import java.util.*;
import java.io.*;

public class LemonadeLine {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("lemonade.in"));
        int N = input.nextInt();
        Integer[] times = new Integer[N]; for (int i = 0; i < N; i++) {
            times[i] = input.nextInt();
        }
        input.close();
        Arrays.sort(times, Comparator.reverseOrder());

        int c = 0;
        for (int i = 0; i < N; i++) if (times[i] >= i) c++;

        PrintWriter output = new PrintWriter(new File("lemonade.out"));
        output.println(c);
        output.close();
    }
}
