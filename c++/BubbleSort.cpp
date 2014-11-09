/**
 * Created by slalos on 11/2/14.
 */
#include <iostream>
#include <math.h>

using namespace std;

int main (void) {

    int size;
    int *array;
    int i, j, k, tmp;
    srand ( time(NULL) );
    cout << "Please give the size of the array to construct..." << endl;
    cin >> size ;
    cout << "The size will be " << size <<  endl; 

    array = new int[size];
    // create the random array
    for ( int i = 0; i < size; i++ ) {
        array[i] = rand()%20;
    }
    // Bubble Sort
    for ( i = 0; i < size; i++) {

        for ( k = 0; k < (size - i); k++ ) {
            if ( array[k] > array[k+1] ) {
                tmp = array[k+1];
                array[k+1] = array[k];
                array[k] = tmp;
            }    
        }
        //print array
        for ( j = 0; j < size; j++ ) {
            cout << array[j] << " ";
        }
        cout << endl;

    }
    return 0;
}
