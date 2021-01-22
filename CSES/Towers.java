import java.util.*;
import java.io.*;

public class Towers {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(input.readLine());
        String[] line = input.readLine().split(" ");
        int[] cubes = new int[N]; for (int i = 0; i < N; i++) cubes[i] = Integer.parseInt(line[i]);
        input.close();
        
        ArrayList<Integer> stacks = new ArrayList<Integer>();
        int lo, up, y;
        for (int cube: cubes) {
            lo = 0; up = stacks.size();
            while (lo < up) {
                y = (lo+up)/2;
                if (cube < stacks.get(y)) up=y;
                else lo=y+1;
            }
            if (up >= stacks.size()) stacks.add(cube);
            else stacks.set(up, cube);
        }

        System.out.println(stacks.size());
    }
}