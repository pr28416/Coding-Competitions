import java.sql.PreparedStatement;
import java.util.*;

public class tlines {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        Coord[] coordinates = new Coord[N];

        for (int i = 0; i < N; i++) {
            coordinates[i] = new Coord(input.nextInt(), input.nextInt());
        }

        input.close();

        // for (Coord c: coordinates) System.out.println(c);
        boolean shouldContinue = true;
        HashSet<Integer> parallels = new HashSet<Integer>();
        
        // Case 1: All parallel (x = k)
        if (shouldContinue) {
            for (Coord c: coordinates) {
                if (parallels.size() > 3) break;
                parallels.add(c.x);
            }
            
            if (parallels.size() <= 3) shouldContinue = false;
        }
        
        parallels.clear();
        
        // Case 2: All parallel (y = k)
        if (shouldContinue) {
            for (Coord c: coordinates) {
                if (parallels.size() > 3) break;
                parallels.add(c.y);
            }
            
            if (parallels.size() <= 3) shouldContinue = false;
        }
        
        parallels.clear();
        
        // Case 3: Two parallel (x = k), one perpendicular (y = k)
        HashMap<Integer, Integer> perpendicular = new HashMap<Integer, Integer>();

        if (shouldContinue) {
            for (Coord c: coordinates) {
                if (!perpendicular.containsKey(c.y)) perpendicular.put(c.y, 0);
                perpendicular.put(c.y, perpendicular.get(c.y) + 1);
            }
            int maxFrequency = 0, maxY = 0;
            for (Map.Entry<Integer, Integer> entry: perpendicular.entrySet()) {
                if (entry.getValue() > maxFrequency) {
                    maxFrequency = entry.getValue();
                    maxY = entry.getKey();
                }
            }
            for (Coord c: coordinates) {
                if (parallels.size() > 2) break;
                if (c.y != maxY) parallels.add(c.x);
            }

            if (parallels.size() <= 2) shouldContinue = false;
        }

        perpendicular.clear();
        parallels.clear();
        // Case 4: Two parallel (y = k), one perpendicular (x = k)
        if (shouldContinue) {
            for (Coord c: coordinates) {
                if (!perpendicular.containsKey(c.x)) perpendicular.put(c.x, 0);
                perpendicular.put(c.x, perpendicular.get(c.x) + 1);
            }
            int maxFrequency = 0, maxX = 0;
            for (Map.Entry<Integer, Integer> entry: perpendicular.entrySet()) {
                if (entry.getValue() > maxFrequency) {
                    maxFrequency = entry.getValue();
                    maxX = entry.getKey();
                }
            }
            for (Coord c: coordinates) {
                if (parallels.size() > 2) break;
                if (c.x != maxX) parallels.add(c.y);
            }

            if (parallels.size() <= 2) shouldContinue = false;
        }

        perpendicular.clear();
        parallels.clear();

        System.out.println(!shouldContinue ? 1 : 0);
    }

    public static class Coord {
        int x, y;
        public Coord(int x, int y) {
            this.x = x; this.y = y;
        }
        public String toString() {
            return String.format("(%s, %s)", x, y);
        }
    }
}
