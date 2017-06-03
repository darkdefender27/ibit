import java.util.Scanner;

public class Main {

    public static void main(String []args) {
        int N, T;
        String s1, s2;
        Scanner sc= new Scanner(System.in);
        T = sc.nextInt();
        while(T > 0) {
            N = sc.nextInt();
            s1 = sc.next();
            s2 = sc.next();
            int [][] plates = new int[2][N];
            for (int i=0; i<N; i++){
                if(s1.charAt(i) == '.'){
                    plates[0][i] = 0;
                }
                else {
                    plates[0][i] = 1;
                }
                if(s2.charAt(i) == '.'){
                    plates[1][i] = 0;
                }
                else {
                    plates[1][i] = 1;
                }
            }
            boolean ret = isLegendTrue(N, plates);
            if(ret)
                System.out.println("yes");
            else
                System.out.println("no");
            T--;
        }
    }

    public static boolean isLegendTrue(int n, int[][] plate) {

        int j=0;
        int index = -1;
        boolean found = false;
        while(j<n && plate[0][j] == 0 && plate [1][j] == 0) {
            j++;
        }
        while(j<n && plate[0][j] == 1 && plate [1][j] == 1) {
            found = true;
            j++;
        }
        if(j == n)
            return found;

        found = true;
        if(plate[0][j] == 1)
            index = 0;
        if(plate[1][j] == 1)
            index = 1;
        if(index == -1){
            while(j<n){
                    if(plate[0][j]==1 || plate[1][j] == 1)
                        found = false;
                    j++;
                }
        }
        j++;
        while(j<n){
            if(plate[index%2][j] == 1){
                if(plate[(index+1)%2][j] == 1)
                    index = index+1;
                j++;
            }
            else{
                while(j<n){
                    if(plate[0][j]==1 || plate[1][j] == 1)
                        found = false;
                    j++;
                }
            }
        }
        return found;
    }
}