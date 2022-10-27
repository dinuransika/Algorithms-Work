import java.util.HashMap;
import java.util.Set;

public class anagramCheck {
    static boolean isAnagram(String a, String b){
        if(a.length()!=b.length()) return false;
        HashMap <Character, Integer> map = new HashMap<>();
        for(int i=0; i<a.length(); i++){
            Character chr = a.charAt(i);
            if(map.containsKey(chr)) map.put(chr, map.get(chr)+1);
            else map.put(chr, 1);
        }
        for(int i=0; i<b.length(); i++){
            Character chr = b.charAt(i);
            if(map.containsKey(chr)) map.put(chr, map.get(chr)-1);
            else return false;
        }
        Set<Character> keys = map.keySet();
        for(Character key:keys){
            if(map.get(key)!=0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        String a = "dinura";
        String b = "riduna";
        System.out.println(isAnagram(a, b));
    }
}
