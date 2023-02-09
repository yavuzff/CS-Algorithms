import javafx.util.Pair;
import java.util.HashMap;

// call using LongestCommonSubsequence.find(s1, s2)
public class LongestCommonSubsequence{
    private static HashMap<Pair<Integer,Integer>, String> memoization = new HashMap<Pair<Integer,Integer>, String>();

    public static String find (String s1,String s2){

        return sub (s1, s2, s1.length()-1,s2.length()-1);
    }

    private static String sub(String s1, String s2, int i, int j){

        if (i==0 || j == 0){
            return "";
        }
        else if (memoization.containsKey(new Pair<>(i,j))) {
            return memoization.get(new Pair<>(i,j));
        }
        else if ((s1.charAt(i) == s2.charAt(j))) {
            String result = sub(s1,s2,i-1,j-1) + s1.charAt(i);
            memoization.put(new Pair<>(i,j),result);
            return result;
        }
        else {
            String opt1 = sub(s1,s2,i-1,j);
            String opt2 = sub(s1,s2,i,j-1);
            if (opt1.length() > opt2.length()) {
                memoization.put(new Pair<>(i,j),opt1);
            }
            else {
                memoization.put(new Pair<>(i,j),opt2);
            }
            return memoization.get(new Pair<>(i,j));
        }

    }
}