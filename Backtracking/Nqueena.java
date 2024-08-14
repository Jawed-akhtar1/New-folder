import java.util.*;
public class Nqueena {
    public static boolean isSafe(char arr[][],int row,int col){
        //vertical up
        for(int i=row-1;i>=0;i--){
            if(arr[i][col]=='Q'){
                return false;
            }
        }
        //diag left up
        for(int i=row-1,j=col-1;i>=0&&j>=0;i--,j--){
            if(arr[i][j]=='Q'){
                return false;
            }
        }
        //diag right up
        for(int i=row-1,j=col+1;i>=0&&j<arr.length;i--,j++){
            if(arr[i][j]=='Q'){
                return false;
            }
        }
        return true;
    }
    public static void queen(char arr[][],int row){
        if(row==arr.length){
            print(arr);
            count++;
            return;
        }
        for(int i=0;i<arr.length;i++){
            if(isSafe(arr,row,i)){
                arr[row][i]='Q';
                queen(arr,row+1);
                arr[row][i]='X';
            }
           
        }
    }
    static int count=0;
    public static void print(char arr[][]){
        System.out.println("----------------chess board--------------------");
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr.length;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void main(String args[]){
        int n=5;
        char arr[][]=new char[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                arr[i][j]='X';
            }
        }
        queen(arr,0);
        System.out.println(count);
    }
}
