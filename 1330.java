import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A,B =0;
        A = sc.nextInt();
        B = sc.nextInt();
        
        if(A>B) {
            System.out.println(">");
        } else if(A < B) {
            System.out.println("<");
        } else if (A==B) {
            System.out.println("==");
        }     
    }
}
