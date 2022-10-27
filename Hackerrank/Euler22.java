import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;



public class Solution {
    public static int getScore(String name){
        int score = 0;
        for(int i = 0; i < name.length(); i++){
            score += name.charAt(i) - 'A' + 1;
        }
        return score;
    }

    public static void main(String[] args) {
        int N;
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        String[] names = new String[N];
        for(int i = 0; i < N; i++){
            names[i] = in.next();
        }
        Arrays.sort(names);
        int Q;
        Q = in.nextInt();
        String[] queries = new String[Q];
        int scores = 0;
        int position;
        for(int i=0; i<Q; i++){
            queries[i] = in.next();
            position = Arrays.binarySearch(names, queries[i]);
            scores = (position+1)*getScore(queries[i]);
            System.out.println(scores);
        }
    }
}