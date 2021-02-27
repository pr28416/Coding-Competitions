import java.lang.reflect.Array;
import java.util.*;

public class YearOfTheCow {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt(), K = input.nextInt();
        int[] years = new int[N];
        for (int i = 0; i < N; i++) {
            years[i] = input.nextInt();
        }
        Arrays.sort(years);
        System.out.println(Arrays.toString(years));
        Set<Integer> ep = new TreeSet<Integer>();
        for (int i = N-1; i >= 0; i--) {
            double div = years[i] / 12.0;
            ep.add(-12*(int)Math.ceil(div));
            ep.add(-12*(int)Math.floor(div));
        }
        Node ep2 = null;
        Node trav = ep2;
        for (int i: ep) {
            if (trav == null) {
                ep2 = new Node(-i);
                trav = ep2;
            } else {
                trav.next = new Node(-i);
                trav = trav.next;
            }
        }

        trav = ep2;
        while (trav != null && trav.next != null && trav.next.next != null) {
            if (trav.item - trav.next)
        }

        ArrayList<Integer> endpoints = new ArrayList<Integer>();
        trav = ep2;
        while (trav != null) {
            endpoints.add(trav.item);
            trav = trav.next;
        }
        
        System.out.println(endpoints);
    }

    static class Node {
        int item; Node next;
        Node(int _item) {
            item = _item;
        }
    }
}
