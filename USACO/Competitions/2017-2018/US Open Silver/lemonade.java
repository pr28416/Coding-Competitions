import java.util.*;
import java.io.*;

public class lemonade {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new FileReader(new File("lemonade.in")));
        int N = Integer.parseInt(input.readLine());
        int[] wList = new int[N];
        String[] line = input.readLine().split(" ");
        input.close();

        for (int i = 0; i < N; i++) {
            wList[i] = Integer.parseInt(line[i]);
        }
        Arrays.sort(wList);
        int tmp;
        for (int i = 0; i < (N+1)/2; i++) {
            tmp = wList[N-i-1];
            wList[N-i-1] = wList[i];
            wList[i] = tmp;
        }

        int k = 0, c = 0;
        for (int i: wList) {
            if (k <= i) {c++;k++;}
        }

        PrintWriter output = new PrintWriter(new File("lemonade.out"));
        output.println(c);
        output.close();
    }    
}
