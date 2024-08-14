import java.util.*;
public class Findsubset {
    public static void main(String args[]){
        String str="abc";
        find(str,"",0);
    }
    public static void find(String str,String ans,int i){
        // Findsubset s=new Findsubset();
        if(i==str.length()){
            if(ans.length()==0){
                System.out.println("null");
            }
            else{
                System.out.println(ans);
            }
           
            return;
        }
        find(str,ans+str.charAt(i),i+1);
        find(str,ans,i+1);
    }
}
