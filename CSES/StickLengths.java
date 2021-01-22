import java.util.*;

public class StickLengths {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int N = input.nextInt();
        long[] nums = new long[N];
        long median;
        for (int i = 0; i < N; i++) nums[i] = input.nextInt();
        input.close();

        Arrays.sort(nums);
        median = nums[N/2];

        long a = 0, b = 0;        
        for (long i: nums) a += Math.abs((long)median-i);
        for (long i: nums) b += Math.abs((long)(median+0.5)-i);
        System.out.println(Long.min(a, b));
    }
}