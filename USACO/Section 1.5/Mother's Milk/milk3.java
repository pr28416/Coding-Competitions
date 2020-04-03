/*
ID: pranav.19
LANG: JAVA
TASK: milk3
*/

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.io.IOException;

class milk3 {
    public static void main(String[] args) throws IOException {

        int A_capacity = 0;
        int B_capacity = 0;
        int C_capacity = 0;

        BufferedReader f = new BufferedReader(new FileReader("milk3.in"));
        PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("milk3.out")));

        String[] temp = f.readLine().split(" ");
        A_capacity = Integer.parseInt(temp[0]);
        B_capacity = Integer.parseInt(temp[1]);
        C_capacity = Integer.parseInt(temp[2]);

        // Setting up the buckets; A and B are empty while C is full
        int bucketA = 0;
        int bucketB = 0;
        int bucketC = C_capacity;

        System.out.println(""+A_capacity+B_capacity+C_capacity);

        f.close();
        out.close();

    }
}