import java.util.*;
public class Permutation {
    public static void main(String args[]){
        String str="abcd";
        permutat(str,"");
    }
    public static void permutat(String str,String ans){
        if(str.length()==0){
            System.out.println(ans);
            return;
        }
        for(int i=0;i<str.length();i++){
            char curr=str.charAt(i);
            String newstr=str.substring(0, i)+str.substring(i+1);
            permutat(newstr,ans+curr);
        }
        
    }
}
