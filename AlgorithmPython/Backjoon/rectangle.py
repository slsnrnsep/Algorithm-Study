import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution {
    public long solution(int[][] rectangles) {
        int count = 0;
        int maxwidth=0;
        int maxheight=0;
        int maxplussize = 0;
        for(int i=0; i< rectangles.length;i++)
        {
            if(maxwidth < rectangles[i][2])
                maxwidth = rectangles[i][2];
            if(maxheight < rectangles[i][3])
                maxheight = rectangles[i][3];
            int width2 = 0;
            int height = 0;
            int sizing = 0;
//            int width22 = rectangles[i][2];
//            int height22 = rectangles[i][3];
//            int[] first={rectangles[i][0],rectangles[i][1]};
//            int[] second={rectangles[i][2]-1,rectangles[i][3]-1};
            width2 = rectangles[i][2] - rectangles[i][0];
            height = rectangles[i][3] - rectangles[i][1];
            sizing = width2 * height;
            maxplussize += sizing;
        }
        int[][] dp= new int[maxheight][maxwidth];

        for (int i = 0; i < rectangles.length; i++) {

            for (int a = rectangles[i][0]; a < rectangles[i][2]; a++) {
                for (int b = rectangles[i][1]; b< rectangles[i][3]; b++) {
                    dp[b][a] += 1;
                    if(dp[b][a]>1)
                        count++;
                }
            }
//            System.out.println(first);
//            System.out.println(second);

//            System.out.println(maxplussize);


//            for (int j = 0; j < rectangles[i].length; j++) {
////                System.out.println(rectangles[i][j]);
//            }
//            System.out.println(dp.length);
        }
//        for (int i=0; i< dp.length; i++)
//            for(int j=0; j<dp[i].length;j++)
//                if(dp[i][j]>1)
//                    count+=dp[i][j]-1;
//
//
////        Arrays.sort(dp,((o1, o2) -> (o1[2]-o2[2])));
//        Arrays.sort(dp, new Comparator<int[]>() {
//            @Override
//            public int compare(int[] o1, int[] o2) {
//                if(o1[0] == o2[0]) {
//                    return o1[1] - o2[1];
//                }else {
//                    return o1[0] - o2[0];
//                }
//            }
//        });

//      System.out.println(dp.length);
        return maxplussize-count;
    }
}

class Main {
    public static void main(String[] args) {
        int[][] arr = {{1, 1, 6, 5}, {2, 0, 4, 2}, {2, 4, 5, 7}, {4, 3, 8, 6}, {7, 5, 9, 7}} ;
        Solution sol = new Solution();
        System.out.println(sol.solution(arr));
    }
}
