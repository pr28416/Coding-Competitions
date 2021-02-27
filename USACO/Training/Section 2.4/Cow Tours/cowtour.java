import java.util.*;
import java.io.*;

public class cowtour {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner input = new Scanner(new File("cowtour.in"));
        int N = input.nextInt();
        Node[] nodes = new Node[N];
        for (int i = 0; i < N; i++) {
            nodes[i] = new Node(input.nextInt(), input.nextInt(), -1, i);
        }

        for (int i = 0; i < N; i++) {
            String line = input.next();
            for (int j = 0; j < N; j++) {
                if (line.charAt(j) == '1') {
                    nodes[i].neighbors.add(nodes[j]);
                }
            }
        }
        input.close();

        int k = 0;
        for (int i = 0; i < N; i++) {
            if (nodes[i].group != -1) continue;
            Queue<Node> queue = new LinkedList<Node>();
            queue.add(nodes[i]);
            while (!queue.isEmpty()) {
                Node item = queue.remove();
                item.group = k;
                item.visited = true;
                for (Node n: item.neighbors) {
                    if (!n.visited) {
                        queue.add(n);
                    }
                }
            }
            k += 1;
            nodes[i].clear();
        }

        for (Node n: nodes) {
            System.out.println("Node: " + n);
            for (Node ne: n.neighbors) {
                System.out.println("\t" + ne);
            }
        }

        // Test Djikstra
        System.out.println(djikstra(nodes, 0));

        // Djikstra
        // double res = Double.MAX_VALUE;
        // for (int i = 0; i < N-1; i++) {
        //     for (int j = i+1; j < N; j++) {
        //         if (nodes[i].group == nodes[j].group) continue;
        //         nodes[i].neighbors.add(nodes[j]);
        //         nodes[j].neighbors.add(nodes[i]);
        //         // Do Djikstra's
        //         res = Double.min(res, djikstra(nodes, i));
        //         nodes[i].neighbors.removeLast();
        //         nodes[j].neighbors.removeLast();
        //     }
        // }
    }

    public static Double djikstra(Node[] nodes, int st) {
        double[] buckets = new double[nodes.length];
        Arrays.fill(buckets, Double.POSITIVE_INFINITY);
        HashSet<Integer> hset = new HashSet<Integer>();
        for (int i = 0; i < nodes.length; i++) hset.add(i);

        double largest = 0;
        buckets[st] = 0;
        int checkpoint = st;
        Integer nextSmallest;

        while (true) {
            System.out.println(checkpoint);
            hset.remove(checkpoint);
            nextSmallest = null;
            for (Node nb: nodes[checkpoint].neighbors) {
                buckets[nb.id] = Double.min(
                    buckets[nb.id],
                    buckets[checkpoint] + nodes[checkpoint].distanceTo(nb)
                );
                // largest = Double.max(buckets[nb.id], largest);
                if ((nextSmallest == null || buckets[nb.id] < buckets[nextSmallest]) && hset.contains(nb.id)) {
                    nextSmallest = nb.id;
                }
            }

            if (nextSmallest == null) {
                break;
            }
        }

        for (int i = 0; i < buckets.length; i++) {
            if (buckets[i] == Double.POSITIVE_INFINITY) continue;
            largest = Double.max(largest, buckets[i]);
        }

        return largest;
    }

    static class Node {
        LinkedList<Node> neighbors;
        long x, y;
        int group, id;
        boolean visited;
        Node(long _x, long _y, int _group, int _id) {
            x = _x; y = _y; group = _group; id = _id;
            neighbors = new LinkedList<Node>();
            visited = false;
        }

        public double squaredDistanceTo(Node other) {
            return (x-other.x)*(x-other.x)+(y-other.y)*(y-other.y);
        }

        public double distanceTo(Node other) {
            return Math.sqrt(squaredDistanceTo(other));
        }

        public void clear() {
            visited = false;
            for (Node i: neighbors) {
                if (i.visited) i.clear();
            }
        }

        public String toString() {
            return String.format("(x:%s, y:%s, grp:%s, id:%s)", x, y, group, id);
        }
    }
}