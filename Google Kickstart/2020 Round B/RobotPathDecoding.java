import java.util.*;

public class RobotPathDecoding {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int T = input.nextInt();
        for (int t = 1; t <= T; t++) {
            Stack<Integer> multiplierStack = new Stack<Integer>();
            Stack<Coord> coordStack = new Stack<Coord>();
            multiplierStack.push(1);
            coordStack.push(new Coord(0, 0));
            String instructions = input.next();
            for (int i = 0; i < instructions.length(); i++) {
                // NSWE
                if (instructions.charAt(i) == 'N') {
                    coordStack.peek().r -= 1;
                } else if (instructions.charAt(i) == 'S') {
                    coordStack.peek().r += 1;
                } else if (instructions.charAt(i) == 'W') {
                    coordStack.peek().c -= 1;
                } else if (instructions.charAt(i) == 'E') {
                    coordStack.peek().c += 1;
                }

                // Integer
                else if ((int)instructions.charAt(i) >= 50 && (int)instructions.charAt(i) <= 57) {
                    multiplierStack.push(instructions.charAt(i)-48);
                    coordStack.push(new Coord(0, 0));
                }

                // Closing parenthesis
                else if (instructions.charAt(i) == ')') {
                    int multiplier = multiplierStack.pop();
                    Coord removed = coordStack.pop();
                    coordStack.peek().r += multiplier * removed.r;
                    coordStack.peek().c += multiplier * removed.c;
                }
            }

            int E9 = 1000000000;
            System.out.printf("Case #%s: %s %s\n",
                t,
                Math.floorMod(coordStack.peek().c, E9)+1,
                Math.floorMod(coordStack.peek().r, E9)+1
                // (coordStack.peek().c%E9+E9)%E9+1,
                // (coordStack.peek().r%E9+E9)%E9+1
            );
        }
        input.close();
    }

    static class Coord {
        int r, c;
        Coord(int _r, int _c) {
            r = _r;
            c = _c;
        }
        void changePos(int down, int right) {
            r = (r+down) % 1000000000;
            c = (c+right) % 1000000000;
        }
    }
}

/*

NWN3(S2(E))
= 1(NWN)3(S2(E))

1: (-2, -1)



*/