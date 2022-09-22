public class test{


    public static void main(String[] args){
        int s = 0;
        int n = 5;
        for(int i = 0; i <= 2 * n; i += 5){            
            System.out.println("FOR 1 ---------------");
            for(int j = i; j <= 2*i; i++){
                System.out.println("   FOR 2 ------------");
                s++;
            }
        }

    }


}