import java.util.*;

public class pasture {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        Coord[] coordinates = new Coord[N];
        for (int i = 0; i < N; i++) {
            coordinates[i] = new Coord(input.nextInt(), input.nextInt());
        }
        input.close();
        // Total for 0 coords, 1 coord, 2 coords
        int total = N+1+(N*(N-1)/2);
        // System.out.println(total);
        // System.out.println(new Coord(1, 2).equals(new Coord(1, 2)));
        // System.out.println("After 012: " + total);

        // 3 coords
        for (int i = 0; i < coordinates.length-2; i++) {
            for (int j = i+1; j < coordinates.length-1; j++) {
                for (int k = j+1; k < coordinates.length; k++) {
                    Coord[] bounds = getBounds(coordinates[i], coordinates[j], coordinates[k]);
                    // Case 1: Compare lower left to upper right
                    Coord[] otherBounds = {
                        new Coord(bounds[0].x, bounds[1].y),
                        new Coord(bounds[1].x, bounds[0].y),
                    };

                    // System.out.printf("Coordinates: %s, %s, %s. Bounds: %s, %s, %s, %s\n",
                    //     coordinates[i], coordinates[j], coordinates[k],
                    //     bounds[0], otherBounds[0], bounds[1], otherBounds[1]
                    // );

                    if (coordinates[i].equals(bounds[0])) {
                        if (coordinates[j].equals(bounds[1])) continue;
                        if (coordinates[k].equals(bounds[1])) continue;
                    }

                    if (coordinates[j].equals(bounds[0])) {
                        if (coordinates[i].equals(bounds[1])) continue;
                        if (coordinates[k].equals(bounds[1])) continue;
                    }

                    if (coordinates[k].equals(bounds[0])) {
                        if (coordinates[j].equals(bounds[1])) continue;
                        if (coordinates[i].equals(bounds[1])) continue;
                    }

                    if (coordinates[i].equals(otherBounds[0])) {
                        if (coordinates[j].equals(otherBounds[1])) continue;
                        if (coordinates[k].equals(otherBounds[1])) continue;
                    }

                    if (coordinates[j].equals(otherBounds[0])) {
                        if (coordinates[i].equals(otherBounds[1])) continue;
                        if (coordinates[k].equals(otherBounds[1])) continue;
                    }

                    if (coordinates[k].equals(otherBounds[0])) {
                        if (coordinates[j].equals(otherBounds[1])) continue;
                        if (coordinates[i].equals(otherBounds[1])) continue;
                    }
                    total++;
                }
            }
        }

        // System.out.println("After 3: " + total);

        // 4 coords
        for (int i = 0; i < coordinates.length-3; i++) {
            for (int j = i+1; j < coordinates.length-2; j++) {
                for (int k = j+1; k < coordinates.length-1; k++) {
                    for (int l = k+1; l < coordinates.length; l++) {
                        Coord[] bounds = getBounds(coordinates[i], coordinates[j], coordinates[k], coordinates[l]);
                        // Case 1: Compare lower left to upper right
                        Coord[] otherBounds = {
                            new Coord(bounds[0].x, bounds[1].y),
                            new Coord(bounds[1].x, bounds[0].y),
                        };
    
                        if (coordinates[i].equals(bounds[0])) continue;
                        if (coordinates[j].equals(bounds[0])) continue;
                        if (coordinates[k].equals(bounds[0])) continue;
                        if (coordinates[l].equals(bounds[0])) continue;
                        if (coordinates[i].equals(bounds[1])) continue;
                        if (coordinates[j].equals(bounds[1])) continue;
                        if (coordinates[k].equals(bounds[1])) continue;
                        if (coordinates[l].equals(bounds[1])) continue;
                        
                        if (coordinates[i].equals(otherBounds[0])) continue;
                        if (coordinates[j].equals(otherBounds[0])) continue;
                        if (coordinates[k].equals(otherBounds[0])) continue;
                        if (coordinates[l].equals(otherBounds[0])) continue;
                        if (coordinates[i].equals(otherBounds[1])) continue;
                        if (coordinates[j].equals(otherBounds[1])) continue;
                        if (coordinates[k].equals(otherBounds[1])) continue;
                        if (coordinates[l].equals(otherBounds[1])) continue;
                        
                        total++;
                    }
                }
            }
        }

        System.out.println(total);
    }

    // static boolean xor(boolean a, boolean b) {
    //     return a && !b || !a && b;
    // }

    static class Coord {
        int x, y;
        public Coord(int _x, int _y) {
            x = _x; y = _y;
        }
        public String toString() {
            return String.format("(%s, %s)", x, y);
        }

        @Override
        public boolean equals(Object o) {
            Coord other = (Coord) o;
            return x == other.x && y == other.y;
        }
    }


    static Coord[] getBounds(Coord a, Coord b, Coord c) {
        return new Coord[]{
            new Coord(Integer.min(c.x, Integer.min(a.x, b.x)), Integer.min(c.y, Integer.min(a.y, b.y))),
            new Coord(Integer.max(c.x, Integer.max(a.x, b.x)), Integer.max(c.y, Integer.max(a.y, b.y))),
        };
    }

    static Coord[] getBounds(Coord a, Coord b, Coord c, Coord d) {
        return new Coord[]{
            new Coord(Integer.min(d.x, Integer.min(c.x, Integer.min(a.x, b.x))), Integer.min(d.y, Integer.min(c.y, Integer.min(a.y, b.y)))),
            new Coord(Integer.max(d.x, Integer.max(c.x, Integer.max(a.x, b.x))), Integer.max(d.y, Integer.max(c.y, Integer.max(a.y, b.y)))),
        };
    }
}
