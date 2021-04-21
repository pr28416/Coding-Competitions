import java.util.Scanner;

class Problem3 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Problem 3 - Rearranging letters in a sequence. Enter input:");
        int n = Integer.parseInt(input.nextLine());
        String[] words = new String[n];
        for (int i = 0; i < n; i++) {
            String a = input.nextLine();
            words[i] = a;
        }

        String fin = "";
        String punctuation = "!()-[]{}:;'\".,?";
        for (String str: words) {
            String[] word = str.split("");
            int lowerBound = 1;
            int upperBound = word.length-1;
            if (punctuation.contains(word[word.length-1])) {
                upperBound --;
            }
            for (int i = lowerBound; i < (upperBound+lowerBound)/2; i++) {
                // System.out.println(String.format("swapping %s and %s", word[i], word[upperBound-i]));
                String temp = word[i];
                word[i] = word[upperBound-i];
                word[upperBound-i] = temp;
                // System.out.println(String.format("\tresult: %s and %s", word[i], word[upperBound-i]));
            }
            String s = "";
            for (String i: word) {
                s += i;
            }
            fin += s+" ";
            // System.out.println("word==>\t"+s+" ");
        }
        fin = fin.substring(0, fin.length()-1);
        System.out.println("\nAnswer:");
        System.out.println(fin);
    }
}