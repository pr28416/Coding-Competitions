import java.io.*;
import java.util.*;
public class maze1 {
    public static void main(String[] args) throws IOException {
        BufferedReader fin = new BufferedReader(new FileReader(new File("maze1.in")));
        PrintWriter fout = new PrintWriter(new File("maze1.out"));

        String[] temp = fin.readLine().split(" ");
        int W = Integer.parseInt(temp[0]), H = Integer.parseInt(temp[1]);

        // NODES
        Node[][] nodes = new Node[H][W];
        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++)
                nodes[i][j] = new Node(i, j);

        // PRE
        char[][] pre = new char[2*H+1][2*W+1];
        for (int i = 0; i < 2*H+1; i++) {
            String t = fin.readLine();
            for (int j = 0; j < 2*W+1; j++)
                pre[i][j] = t.charAt(j);
        }
        for (int i = 0; i < 2*H+1; i++) {
            for (int j = 0; j < 2*W+1; j++)
                System.out.print(pre[i][j]);
            System.out.println();
        }

        // Define boundaries per node
        Node[] openings = new Node[2];
        int i = 0;

        for (int h = 0; h < H; h++) {
            for (int w = 0; w < W; w++) {
                // Left
                if (pre[2*h+1][2*w] != '|') {
                    if (w == 0) openings[i++] = nodes[h][w];
                    else nodes[h][w].addNeighbor(nodes[h][w-1]);
                }
                // Right
                if (pre[2*h+1][2*w+2] != '|') {
                    if (w == W-1) openings[i++] = nodes[h][w];
                    else nodes[h][w].addNeighbor(nodes[h][w+1]);
                }
                // Up
                if (pre[2*h][2*w+1] != '-') {
                    if (h == 0) openings[i++] = nodes[h][w];
                    else nodes[h][w].addNeighbor(nodes[h-1][w]);
                }
                // Down
                if (pre[2*h+2][2*w+1] != '-') {
                    if (h == H-1) openings[i++] = nodes[h][w];
                    else nodes[h][w].addNeighbor(nodes[h+1][w]);
                }
            }
        }

        System.out.println("Openings: " + Arrays.toString(openings));

        // Test openings
        for (i = 0; i < 2; i++) {
            Node root = openings[i];
            Queue<Node> qu = new LinkedList<Node>();
            qu.add(root);
            Node cur;
            while (qu.size() > 0) {
                cur = qu.remove();
                for (int n = 0; n < cur.neighbors.length; n++) {
                    Node neighbor = cur.neighbors[n];
                    if (neighbor == null) continue;
                    if (!neighbor.didCheck
                    || neighbor.didCheck && cur.values[i]+1 < neighbor.values[i]) {
                        neighbor.values[i] = cur.values[i]+1;
                        neighbor.didCheck = true;
                        qu.add(neighbor);
                    }
                }
            }
        }

        for (Node[] n: nodes) {
            System.out.println(Arrays.toString(n));
        }
        

        fin.close();

        fout.close();
    }
}

class Node {
    int h, w;
    boolean didCheck;
    int[] values;
    Node[] neighbors;
    private int nIdx;

    public Node(int h, int w) {
        this.h = h; this.w = w;
        values = new int[]{1, 1};
        neighbors = new Node[4];
    }

    public void addNeighbor(Node node) {
        neighbors[nIdx++] = node;
    }

    public String toString() {
        return String.format("(%s,%s) [%s,%s]", h, w, values[0], values[1]);
        // return String.format("[%s, %s]", values[0], values[1]);
    }
}