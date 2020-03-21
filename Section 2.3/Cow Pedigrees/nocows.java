/*
ID: pranav.19
LANG: JAVA
TASK: nocows
*/

import java.io.*;
import java.util.*;

class nocows {

    // static class Node {
    //     int height = 1; // Max height: K
    //     boolean isMainThread;
    //     Node parent;
    //     ArrayList<Node> children;
    //     public Node(Node parent, boolean isMainThread) {
    //         this.isMainThread = isMainThread;
    //         this.parent = parent;
    //         if (parent != null) {
    //             this.height = parent.height+1;
    //         }
    //         children = new ArrayList<Node>(2);
    //     }
    // }

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
    static SquareNode[] treeChain;

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File("nocows.in")));
        String[] c = reader.readLine().split(" ");
        N = Integer.parseInt(c[0]);
        K = Integer.parseInt(c[1]);
        System.out.println(String.format("N: %d, K: %d", N, K));
        // Create initial tree chain with specified height
        treeChain = new SquareNode[K-1];
        for (int i = 0; i < treeChain.length; i++) {
            if (i == 0) {
                treeChain[i] = new SquareNode();
            } else {
                treeChain[i] = new SquareNode(treeChain[i-1]);
            }
        }

        for (SquareNode i: treeChain) {
            System.out.println(i.height + "\tnch");
        }
        reader.close();
        // fill(treeChain, treeChain.length);
        ArrayList<SquareNode> allNodes = new ArrayList<SquareNode>();
        allNodes.add(new SquareNode());
        span(allNodes, 2);
        System.out.println("total: "+total);
        System.out.println("set size: "+set.size());
    }
    static int total = 0;
    static Set<StringBuilder> set = new HashSet<StringBuilder>();

    public static void span(ArrayList<SquareNode> allNodes, int maxHeight) {
        System.out.println(String.format("numSquares: %s, numSquares*2+1: %s", allNodes.size(), allNodes.size()*2+1));
        if (allNodes.size()*2+1 == N) {
            if (maxHeight == K) {
                StringBuilder i = new StringBuilder();
                for (SquareNode node: allNodes) {
                    i.append((char)node.height);
                }
                set.add(i);
                System.out.println("break");
                total++;
                return;
            } else {
                System.out.println("failed");
                return;
            }
            
        } else {
            for (int i = 0; i < allNodes.size(); i++) {
                if (allNodes.get(i).height < K) {
                    // Assign left if possible
                    if (allNodes.get(i).left == null) {
                        allNodes.get(i).left = new SquareNode(allNodes.get(i));
                        allNodes.add(allNodes.get(i).left);
                        if (allNodes.get(i).left.height > maxHeight) span(allNodes, allNodes.get(i).left.height);
                        else span(allNodes, maxHeight);
                        allNodes.remove(allNodes.size()-1);
                        allNodes.get(i).left = null;
                    }
                    // Assign right if possible
                    if (allNodes.get(i).right == null) {
                        allNodes.get(i).right = new SquareNode(allNodes.get(i));
                        allNodes.add(allNodes.get(i).right);
                        if (allNodes.get(i).right.height > maxHeight) span(allNodes, allNodes.get(i).right.height);
                        else span(allNodes, maxHeight);
                        allNodes.remove(allNodes.size()-1);
                        allNodes.get(i).right = null;
                    }
                }
            }
            return;
        }
    }


    // public static void fill(SquareNode[] nodeList, int numSquares) {
    //     if (numSquares*2+1 == N) {
    //         total++;
    //     } else if (numSquares*2+1 < N) {
    //         for (int i = 0; i < nodeList.length; i++) {
    //             // Make right node
    //             if (nodeList[i].height < K && nodeList[i].right == null) {
    //                 SquareNode temp = nodeList[i];
    //                 nodeList[i] = new SquareNode(temp);
    //                 fill(nodeList, numSquares + 1);
    //                 nodeList[i] = temp;
    //             }
    //             // Make down node
    //             if (nodeList[i].height < K && nodeList[i].down == null) {
    //                 SquareNode temp = nodeList[i];
    //                 nodeList[i] = new SquareNode(temp);
    //                 fill(nodeList, numSquares + 1);
    //                 nodeList[i] = temp;
    //             }
    //         }
    //     }
    // }

}