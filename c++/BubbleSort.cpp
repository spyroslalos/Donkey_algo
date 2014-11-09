/**
 * Created by slalos on 11/2/14.
 */
#include <iostream>
#include <math.h>

using namespace std;

int main (void) {

    int size;
    int *array;
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
    for () {
        //print array
        for ( int i = 0; i < size; i++ ) {
            cout << array[i] << " ";
        }
        cout << endl;

    }
    return 0;
}
