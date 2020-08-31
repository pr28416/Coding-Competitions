import java.io.*;
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


        fin.close();

        fout.close();
    }
}

class Node {
    int h, w;
    boolean didCheck;
    int[] values, neighbors;
    public Node(int h, int w) {
        this.h = h; this.w = w;
        didCheck = false;
        values = new int[]{1, 1};
        neighbors = new int[4];
    }
    public String toString() {
        return String.format("(%s, %s), [%s, %s]", h, w, values[0], values[1]);
    }
}