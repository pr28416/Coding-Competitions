import java.io.*;
import java.util.*;

public class Apartments {
    public static void main(String[] args) throws IOException {
        // Scanner input = new Scanner(System.in);
        BufferedInputStream input = new BufferedInputStream(System.in);
        int N = readInt(input), M = readInt(input), K = readInt(input);
        int[] desired = new int[N]; for (int i = 0; i < N; i++) desired[i] = readInt(input);
        int[] sizes = new int[M]; for (int i = 0; i < M; i++) sizes[i] = readInt(input);
        input.close();
        
        Arrays.sort(desired);
        Arrays.sort(sizes);

        int d = 0, s = 0, c = 0;
        while (d < N && s < M) {
            if (Math.abs(sizes[s]-desired[d]) <= K) {
                c++; d++; s++;
            }
            else if (sizes[s] - desired[d] > K) d++;
            else s++;
        }

        System.out.println(c);
    }

    private static int readInt(InputStream in) throws IOException {
        int ret = 0;
        boolean dig = false;
    
        for (int c = 0; (c = in.read()) != -1; ) {
            if (c >= '0' && c <= '9') {
                dig = true;
                ret = ret * 10 + c - '0';
            } else if (dig) break;
        }
    
        return ret;
    }
}
