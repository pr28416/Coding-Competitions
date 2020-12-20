import java.util.*;
import java.io.*;

public class moobuzz {
    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(new File("moobuzz.in"));
        int N = input.nextInt();
        input.close();
        PrintWriter output = new PrintWriter(new File("moobuzz.out"));
        int[] choices = {1, 2, 4, 7, 8, 11, 13, 14};
        output.println(choices[(N-1)%8] + 15*((N-1)/8));
        output.close();
    }
}