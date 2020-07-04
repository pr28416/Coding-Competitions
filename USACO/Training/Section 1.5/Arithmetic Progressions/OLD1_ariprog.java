/*
ID: pranav.19
LANG: JAVA
TASK: ariprog
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

class OLD1_ariprog {
    public static void main(String[] args) throws IOException {

        double start = (double)System.currentTimeMillis()/1000;

        int N = 0, M = 0;

        BufferedReader f = new BufferedReader(new FileReader("ariprog.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("ariprog.out")));

        N = Integer.parseInt(f.readLine());
        M = Integer.parseInt(f.readLine());

        f.close();

        ArrayList<Integer> bisquares = new ArrayList<Integer>();
        for (int p = 0; p <= M; p++) {
            for (int q = 0; q <= M; q++) {
                if (!bisquares.contains((int)(Math.pow(p, 2)+Math.pow(q, 2)))) {
                    bisquares.add((int)(Math.pow(p, 2)+Math.pow(q, 2)));
                }
            }
        }
        // for (int i:bisquares) {
        //     System.out.print(i+" ");
        // }
        // System.out.println("Initial sort");
        // bisquares = split(bisquares);
        Collections.sort(bisquares);
        // printTime(start);
        for (int i:bisquares) {
            System.out.print(i+" ");
        }
        // System.out.println();

        ArrayList<Integer[]> answers = new ArrayList<Integer[]>();
        int cycles = 0;

        for (int i1 = 0; i1 < bisquares.size(); i1++) {
            int b = bisquares.get(i1);

            if (b+2*(bisquares.get(i1+1)-b) <= bisquares.get(bisquares.size()-1)) {
                for (int c = i1+1; c < bisquares.size(); c++) {

                    if (bisquares.contains(b+2*(bisquares.get(c)-b))) {
                        if (bisquares.get(bisquares.size()-1)-(b+(bisquares.get(c)-b)*(N-1)) >= 0) {
                            int counter = 3;
                            boolean keepGoing = true;

                            while (keepGoing && counter < N) {
                                cycles += 1;
                                keepGoing = false;

                                if (bisquares.contains(b+(bisquares.get(c)-b)*counter)) {
                                    keepGoing = true;
                                    counter += 1;
                                }
                            }

                            if (counter == N) {
                                answers.add(new Integer[] {b, (bisquares.get(c)-b)});
                            }

                        } else {
                            break;
                        }
                    }
                }
            } else {
                break;
            }
        }

        System.out.println("Finished");
        printTime(start);

        if (answers.size() != 0) {
            answers = split(answers);
            for (Integer[] i:answers) {
                System.out.print("("+i[0]+", "+i[1]+"), ");
                out.println(i[0]+" "+i[1]);
            }
        } else {
            System.out.println("NONE");
            out.println("NONE");
        }

        printTime(start);

        out.close();
        System.out.println(cycles+" cycles");

    }

    public static ArrayList<Integer[]> split(ArrayList<Integer[]> x) {
        if (x.size() == 1) {
            return x;
        } else {
            ArrayList<Integer[]> a = new ArrayList<Integer[]>(x.subList(0, (int)x.size()/2));
            ArrayList<Integer[]> b = new ArrayList<Integer[]>(x.subList((int)x.size()/2, x.size()));

            // for (int i = 0; i < (int)x.size()/2; i++) {
            //     a.add(x.get(i));
            //     b.add(x.get(i+(int)x.size()/2));
            // }

            a = split(a);
            b = split(b);

            return merge(a, b);
        }
    }

    public static ArrayList<Integer[]> merge(ArrayList<Integer[]> a, ArrayList<Integer[]> b) {
        ArrayList<Integer[]> x = new ArrayList<Integer[]>();

        int aSize = a.size();
        int bSize = b.size();
        
        while (a.size() > 0 && b.size() > 0) {
            if (a.get(0)[1] < b.get(0)[1]) {
                x.add(a.remove(0));
                aSize--;
            } else if (a.get(0)[1] > b.get(0)[1]) {
                x.add(b.remove(0));
                bSize--;
            } else {
                if (a.get(0)[0] < b.get(0)[0]) {
                    x.add(a.remove(0));
                    aSize--;
                } else {
                    x.add(b.remove(0));
                    bSize--;
                }
            }
        }
        while (aSize > 0) {
            x.add(a.remove(0));
            aSize--;
        }
        while (bSize > 0) {
            x.add(b.remove(0));
            bSize--;
        }
        return x;
    }

    public static void printTime(double start) {
        System.out.println("It took " + ((double)System.currentTimeMillis()/1000 - start) + " seconds");
    }
}