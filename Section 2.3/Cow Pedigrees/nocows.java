/*
ID: pranav.19
LANG: JAVA
TASK: nocows
*/

import java.io.*;
import java.util.*;

class nocows {

    static class Node {
        Node left, right;
        int height;

        public Node(Node parent) {
            height = parent.height+1;
        }

        public Node() {
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
        treeChain = new Node[K-1];
        for (int i = 0; i < treeChain.length; i++) {
            if (i == 0) {
                treeChain[i] = new Node();
            } else {
                treeChain[i] = new Node(treeChain[i-1]);
            }
        }

        for (Node i: treeChain) {
            System.out.println(i.height + "\tnch");
        }
        reader.close();
        // fill(treeChain, treeChain.length);
        ArrayList<Node> allNodes = new ArrayList<Node>();
        allNodes.add(new Node());
        span(allNodes);
        // System.out.println("total: "+total);
        System.out.println(String.format("Set size: %s, total: %s", set.size(), total));

    }
    static int total = 0;
    static Set<StringBuilder> set = new HashSet<StringBuilder>();
    static Set<ArrayList<Node>> used = new HashSet<ArrayList<Node>>();

    public static void span(ArrayList<Node> nodes) {
        if (used.contains(nodes)) return;
        used.add(nodes);
        if (nodes.size()*2+1 == N) {
            // Check for max height
            int height = 0;
            for (Node node: nodes) if (node.height > height) height = node.height;

            if (height != K) {
                System.out.println("nope " + height);
                return;
            }
            System.out.println("found");
            total++;
            set.add(preorder(nodes.get(0), new StringBuilder()));
            return;
        } else {
            // Iterate through all nodes and check if a node can be added
            for (int i = 0; i < nodes.size(); i++) {
                // Make sure height is not K
                if (nodes.get(i).height == K) {
                    System.out.println("node height was K, skip");
                    continue;
                }
                if (nodes.get(i).left != null && nodes.get(i).right != null) {
                    System.out.println("X: Node filled " + nodes.get(i).height);
                }

                // See if left node can be added
                if (nodes.get(i).left == null) {
                    nodes.get(i).left = new Node(nodes.get(i));
                    nodes.add(nodes.get(i).left);
                    System.out.println("O: Added left node "+nodes.get(i).left.height);
                    span(nodes);
                    nodes.get(i).left = null;
                    nodes.remove(i+1);
                }
                

                // See if right node can be added
                if (nodes.get(i).right == null) {
                    nodes.get(i).right = new Node(nodes.get(i));
                    nodes.add(nodes.get(i).right);
                    System.out.println("O: Added right node "+nodes.get(i).right.height);
                    span(nodes);
                    nodes.get(i).right = null;
                    nodes.remove(i+1);
                }
            }
            return;
        }
    }

    public static StringBuilder preorder(Node node, StringBuilder s) {
        // Root left right
        if (node == null) {
            return s;
        }
        s.append(node.height);
        s = preorder(node.left, s);
        s = preorder(node.right, s);
        // s.append(preorder(node.left, s));
        // s.append(preorder(node.right, s));
        return s;
    }

}