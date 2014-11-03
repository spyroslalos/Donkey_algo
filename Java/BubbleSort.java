/**
 * Created by slalos on 11/2/14.
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class BubbleSort {

    public static void main( String []args ) {


        int n, i, j, tmp;
        Scanner in = new Scanner( System.in );

        System.out.println ( "Select number of integers to sort" );
        n = in.nextInt ();

        int array[] = new int[n];

        System.out.println ( "Enter " + n + " integers" );

        for ( i = 0; i < n; i++ )
            array[i] = in.nextInt ();

        for ( i = 0; i < ( n - 1 ); i++ ) {
            for ( j = 0; j < (n - i - 1); j++ ) {
                if ( array[j] > array[j+1] ) {
                    tmp = array[j];
                    array[j] = array[j+1];
                    array[j+1] = tmp;
                }
            }
        }

        System.out.println("Sorted list of numbers");
        System.out.println(Arrays.toString(array));
    }

}
