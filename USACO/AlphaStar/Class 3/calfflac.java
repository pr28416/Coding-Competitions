import java.util.Arrays;
import java.util.Scanner;

public class calfflac {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String string = "", alpha = "abcdefghijklmnopqrstuvwxyz";
        // debug
        // string += input.nextLine() + "\n";
        while (input.hasNextLine()) {
            string += input.nextLine()+"\n";
        }
        // System.out.println(string);
        input.close();

        char[] modArray = new char[2*string.length()-1];
        for (int i = 0; i < modArray.length; i++) {
            modArray[i] = i%2==0 ? string.charAt(i/2) : '#';
        }
        int[] code = new int[modArray.length];
        for (int i = 0; i < code.length; i+=2) {
            if (alpha.indexOf(Character.toLowerCase(modArray[i])) != -1) code[i] = 1;
        }
        // System.out.println(Arrays.toString(modArray));
        // System.out.println(Arrays.toString(code));

        int[] answer = {modArray.length, modArray.length};

        for (int i = 0; i < modArray.length; i++) {
            int[] fin;
            if (i % 2 == 1) fin = new int[]{i-1, i+1};
            else fin = new int[]{i, i};

            int lo = fin[0], up = fin[1];

            while (lo > -1 && up < modArray.length) {
                if (code[lo] == 0) lo -= 2;
                else if (code[up] == 0) up += 2;
                else if (Character.toLowerCase(modArray[lo]) == Character.toLowerCase(modArray[up])) {
                    fin[0] = lo; fin[1] = up;
                    lo -= 2; up += 2;
                } else break;
            }

            if (fin[1]-fin[0]>answer[1]-answer[0]) answer = fin;
            else if (fin[1]-fin[0]==answer[1]-answer[0]&&fin[0]<=answer[0]) answer = fin;
        }

        String ans = "";
        int c = 0;
        for (int i = answer[0]; i <= answer[1]; i+=2) {
            ans += modArray[i];
            if (alpha.indexOf(Character.toLowerCase(modArray[i])) != -1) c+=1;
        }
        System.out.println(c);
        System.out.println(ans);
    }
}