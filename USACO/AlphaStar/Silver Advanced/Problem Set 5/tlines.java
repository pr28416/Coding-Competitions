import java.util.*;

public class tlines {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        Coord[] coordinates = new Coord[N];
        for (int i = 0; i < N; i++) {
            coordinates[i] = new Coord(input.nextInt(), input.nextInt());
        }
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
