import java.util.*;

public class wmorph {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String start = input.next();
        String end = input.next();
        
        Set<String> tmp = new HashSet<String>();
        tmp.add(start);
        tmp.add(end);

        while (input.hasNext()) {
            String e = input.next();
            if (e.length() != start.length()) continue;
            tmp.add(e);
        }
        input.close();

        String[] dictionary = new String[tmp.size()];
        int i = 0;
        for (String s: tmp) dictionary[i++] = s;

        Arrays.sort(dictionary);

        ArrayList<ArrayList<Integer>> table = new ArrayList<ArrayList<Integer>>();
        for (i = 0; i < dictionary.length; i++) {
            table.add(new ArrayList<Integer>());
        }

        for (i = 0; i < dictionary.length-1; i++) {
            outer: for (int j = i+1; j < dictionary.length; j++) {
                int c = 0;
                for (int k = 0; k < start.length(); k++) {
                    if (dictionary[i].charAt(k) != dictionary[j].charAt(k)) c += 1;
                    if (c > 1) continue outer;
                }
                if (c == 1) {
                    if (table.get(i) == null) table.set(i, new ArrayList<Integer>());
                    if (table.get(i) == null) table.set(j, new ArrayList<Integer>());
                    table.get(i).add(j);
                    table.get(j).add(i);
                }
            }
        }

        boolean[] visited = new boolean[table.size()];
        int idx = Arrays.binarySearch(dictionary, start);
        visited[idx] = true;

        Queue<Integer[]> queue = new LinkedList<Integer[]>();
        queue.add(new Integer[]{idx, 0});

        while (!queue.isEmpty()) {
            Integer[] item = queue.remove();

            if (dictionary[item[0]].equals(end)) {
                System.out.println(item[1]);
                break;
            }

            for (int n: table.get(item[0])) {
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(new Integer[]{n, item[1]+1});
                }
            }
        }
    }
}
