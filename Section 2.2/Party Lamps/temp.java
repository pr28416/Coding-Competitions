class temp {
    public static void main(String[] args) {
        recurse(0, 10000);
    }

    static void recurse(int c, int target) {
        System.out.println("Number: "+c);
        if (c == target) {
            return;
        } else {
            recurse(c+1, target);
        }
    }
}