/*
ID: pranav.19
LANG: JAVA
TASK: lamps
*/

class test {
    public static void main(String[] args) {
        for (int i = 0; i < 20; i++) {
            if (i % 2 == 0) {
                continue;
            }
            System.out.print(i+"\t");
        }
    }
}