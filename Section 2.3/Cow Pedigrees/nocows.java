/*
ID: pranav.19
LANG: JAVA
TASK: nocows
*/

import java.io.*;
import java.util.*;

class nocows {

    static class Node {
        int height = 1; // Max height: K
        boolean isMainThread;
        Node parent;
        ArrayList<Node> children;
        public Node(Node parent, boolean isMainThread) {
            this.isMainThread = isMainThread;
            this.parent = parent;
            if (parent != null) {
                this.height = parent.height+1;
            }
            children = new ArrayList<Node>(2);
        }
    }

    static class SquareNode {
        SquareNode left, right;
        int height;

        public SquareNode(SquareNode parent) {
            height = parent.height+1;
        }

        public SquareNode() {
            height = 2;
        }
    }

    // 3 <= N < 200
    // 1 < K < 100
    static int N, K;
    static Node[] treeChain;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File("nocows.in")));
        String[] c = reader.readLine().split(" ");
        N = Integer.parseInt(c[0]);
        K = Integer.parseInt(c[1]);
        System.out.println(String.format("N: %d, K: %d", N, K));
        // Create initial tree chain with specified height
        // treeChain = new Node[K];
        // for (int i = 0; i < treeChain.length; i++) {
        //     if (i == 0) {
        //         treeChain[i] = new Node(null, true);
        //     } else {
        //         treeChain[i] = new Node(treeChain[i-1], true);
        //         treeChain[i-1].children.add(treeChain[i]);
        //     }
        // }

        // for (Node i: treeChain) {
        //     if (i.children.size() != 0) {
        //         System.out.println(i.height + "\tch:" + i.children.get(0).height);
        //     } else {
        //         System.out.println(i.height + "\tnch");
        //     }

        // }

    }

    

}