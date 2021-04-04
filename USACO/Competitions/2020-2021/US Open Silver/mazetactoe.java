import java.util.*;
import java.io.*;

class mazetactoe {

    static int N = 0;
    static thing[][] maze;
    static char[][] grid;
    static int[] boardStates = new int[19683];
    static int wins = 0;
    static int[][] moves = {
        new int[]{1, 0},
        new int[]{-1, 0},
        new int[]{0, 1},
        new int[]{0, -1}
    };
    static HashSet<Integer>[][] visited;

    public static void main(String[] args) throws FileNotFoundException {
        // Scanner input = new Scanner(System.in);
        Scanner input = new Scanner(new File("mazetactoe.in"));
        N = input.nextInt();
        maze = new thing[N][N];
        grid = new char[3][3];
        visited = (HashSet<Integer>[][]) new HashSet[N][N];

        int sR = 0, sC = 0;

        for (int i = 0; i < N; i++) {
            String line = input.next();
            for (int j = 0; j < N; j++) {
                maze[i][j] = new thing(line.charAt(3*j), line.charAt(3*j+1), line.charAt(3*j+2));
                if (line.charAt(3*j) == 'B') {sR = i; sC = j;}
                visited[i][j] = new HashSet<Integer>();
            }
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                grid[i][j] = '.';
            }
        }

        printMaze();
        dfs(sR, sC, grid, 0);
        System.out.println(wins);
    }

    static void dfs(int r, int c, char[][] board, int count) {
        int state = convertBoardState(board);
        if (boardStates[state] > 4) return;
        if (boardStates[state] == 0 && checkIfWon(board)) {
            System.out.println("FOUND");
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    System.out.print(board[i][j]);
                }
                System.out.println();
            }
            wins++;
            boardStates[state] += 1;
            return;
        } else if (checkIfFilled(board)) {
            boardStates[state] += 1;
            return;
        } else if (visited[r][c].contains(state)) {
            return;
        } else {
            visited[r][c].add(state);
            boardStates[state] += 1;
            for (int[] move: moves) {
                int nr = r+move[0], nc = c+move[1];
                if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if (maze[nr][nc].isObstacle) continue;
                if (!maze[nr][nc].isObstacle && !maze[nr][nc].isPath) {
                    thing loc = maze[nr][nc];
                    if (board[loc.r][loc.c] == '.') {
                        board[loc.r][loc.c] = loc.letter;
                        dfs(nr, nc, board, count+1);
                        board[loc.r][loc.c] = '.';
                    } else {
                        dfs(nr, nc, board, count+1);
                    }
                } else if (maze[nr][nc].isPath) {
                    dfs(nr, nc, board, count+1);
                }
            }
            return;
        }
    }

    static char[][] copyBoard(char[][] board) {
        char[][] copy = new char[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                copy[i][j] = board[i][j];
            }
        }
        return copy;
    }

    static void printMaze() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(maze[i][j]);
            }
            System.out.println();
        }
    }

    static class thing {
        boolean isObstacle, isPath;
        char letter;
        int r, c;
        thing(char c1, char c2, char c3) {
            if (c1 == '#') {
                isObstacle = true; isPath = false;
                letter = '#';
                r = -1; c = -1;
            } else if (c1 == '.' || c1 == 'B') {
                isObstacle = false; isPath = true;
                letter = c1;
                r = -1; c = -1;
            } else {
                isObstacle = false; isPath = false;
                letter = c1;
                r = c2 - 49;
                c = c3 - 49;
            }
        }
        public String toString() {
            if (letter == '#') {return "(###)";}
            else if (letter == '.') {return "(...)";}
            else if (letter == 'B') {return "(BBB)";}
            else {
                return String.format("(%s%s%s)", letter, r, c);
            }
        }
    }

    static boolean checkIfWon(char[][] board) {
        for (int i = 0; i < 3; i++) {
            if (board[i][0] == 'M' && board[i][1] == 'O' && board[i][2] == 'O') return true;
            if (board[i][2] == 'M' && board[i][1] == 'O' && board[i][0] == 'O') return true;
            if (board[0][i] == 'M' && board[1][i] == 'O' && board[2][i] == 'O') return true;
            if (board[2][i] == 'M' && board[1][i] == 'O' && board[0][i] == 'O') return true;
        }
        if (board[0][0] == 'M' && board[1][1] == 'O' && board[2][2] == 'O') return true;
        if (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'M') return true;
        if (board[0][2] == 'M' && board[1][1] == 'O' && board[2][0] == 'O') return true;
        if (board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'M') return true;
        return false;
    }

    static boolean checkIfFilled(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == '.') return false;
            }
        }
        return true;
    }

    static int convertBoardState(char[][] board) {
        int val = 0, p = 8;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                int k = board[i][j] == '.' ? 0 : board[i][j] == 'O' ? 1 : 2;
                val += k*(int)Math.pow(3,p);
                p--;
            }
        }
        return val;
    }
}