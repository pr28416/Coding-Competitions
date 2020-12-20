import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.*;

public class berries {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("berries.in"));
        int N = input.nextInt(), K = input.nextInt();
        int[] berries = new int[N];
        for (int i = 0; i < N; i++) berries[i] = input.nextInt();
        input.close();
        // System.out.println(Arrays.toString(berries));
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>((x, y) -> Integer.compare(y, x));
        for (Integer a: berries) {
            if (a == null) continue;
            queue.add(a);
        }

        int max = 0;
        while (true) {
            int bSum = 0;
            LinkedList<Integer> tmp1 = new LinkedList<Integer>();
            LinkedList<Integer> tmp2 = new LinkedList<Integer>();
            for (int i = 0; i < K/2; i++) {
                tmp1.add(queue.poll());
            }
            int size = queue.size();
            for (int i = 0; i < Integer.min(K/2, size); i++) {
                // System.out.println(queue.peek());
                bSum += queue.peek();
                tmp2.add(queue.poll());
            }
            if (bSum >= max) max = bSum;
            else break;

            while (!tmp1.isEmpty()) queue.add(tmp1.remove());
            while (!tmp2.isEmpty()) queue.add(tmp2.remove());

            int head = queue.poll();
            queue.add(head/2);
            queue.add(head-head/2);
        }

        // System.out.println(max);
        PrintWriter output = new PrintWriter(new File("berries.out"));
        output.println(max);
        output.close();
    }
}
