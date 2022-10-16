import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        int[] answer = {};


        for(int i=0; i<numbers.length; i++) {
            for (int j=i+1; j<numbers.length; j++) {
                int num = numbers[i]+numbers[j];
                if (res.contains(num)==false)
                    res.add(num);
            }
        }
        answer = res.stream().mapToInt(i->i).toArray();
        Arrays.sort(answer);
        return answer;
    }
}