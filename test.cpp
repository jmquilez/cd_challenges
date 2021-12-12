#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main() {
    int uno = 32;
    int* ptr = &uno;
    int* alloc;
    alloc = (int*)malloc(sizeof(char));
    alloc[0] = 83;
    alloc[1] = 22;
    alloc[2] = 264;
    int* alloc2;
    alloc2 = (int*)malloc(sizeof(char));
    alloc2[0] = 435;
    alloc2[1] = 6345;
    alloc2[2] = 83420;
    int* alloc3;
    alloc3 = (int*)malloc(sizeof(char));
    alloc3[0] = 435;
    alloc3[1] = 6345;
    alloc3[2] = 83420;
    int* alloc4;
    alloc4 = (int*)malloc(sizeof(char));
    alloc4[0] = 435;
    alloc4[1] = 6345;
    alloc4[2] = 83420;
    int* alloc5;
    alloc5 = (int*)malloc(sizeof(char));
    alloc5[0] = 435;
    alloc5[1] = 6345;
    //if alloc(n)[2] is not assigned a value and we try to print it, the system automatically assigns it a value.
    //This does not happen with alloc(n)[3], which remains at 0 if unset.
    //alloc5[2] = 83420;
    cout << "msize is: " << endl;
    cout << _msize(alloc) << endl;
    cout << "uno allocation" << endl;
    cout << ptr << endl;
    cout << "size of ptr: " << endl;
    cout << sizeof(ptr) << endl;
    cout << "\n\n" << endl;
    cout << "alloc value is: " << endl;
    cout << alloc << endl;
    printf("%d ", alloc[0]);
    cout << "\n";
    cout << sizeof(alloc[0]) << endl;
    printf("%d ", alloc[1]);
    cout << "\n";
    cout << sizeof(alloc[1]) << endl;
    printf("%d ", alloc[2]);
    cout << "\n";
    cout << sizeof(alloc[2]) << endl;
    cout << "" << endl;
    cout << "alloc2 value is: " << endl;
    cout << alloc2 << endl;
    printf("%d ", alloc2[0]);
    cout << "\n";
    cout << sizeof(alloc2[0]) << endl;
    printf("%d ", alloc2[1]);
    cout << "\n";
    cout << sizeof(alloc2[1]) << endl;
    printf("%d ", alloc2[2]);
    cout << "\n";
    cout << sizeof(alloc2[2]) << endl;
    cout << "" << endl;
    cout << "alloc3 value is: " << endl;
    cout << alloc3 << endl;
    printf("%d ", alloc3[0]);
    cout << "\n";
    cout << sizeof(alloc3[0]) << endl;
    printf("%d ", alloc3[1]);
    cout << "\n";
    cout << sizeof(alloc3[1]) << endl;
    printf("%d ", alloc3[2]);
    cout << "\n";
    cout << sizeof(alloc3[2]) << endl;
    cout << "" << endl;
    cout << "alloc4 value is: " << endl;
    cout << alloc4 << endl;
    printf("%d ", alloc4[0]);
    cout << "\n";
    cout << sizeof(alloc4[0]) << endl;
    printf("%d ", alloc4[1]);
    cout << "\n";
    cout << sizeof(alloc4[1]) << endl;
    printf("%d ", alloc4[2]);
    cout << "\n";
    cout << sizeof(alloc4[2]) << endl;
    cout << "" << endl;
    cout << "alloc5 value is: " << endl;
    cout << alloc5 << endl;
    printf("%d ", alloc5[0]);
    cout << "\n";
    cout << sizeof(alloc5[0]) << endl;
    printf("%d ", alloc5[1]);
    cout << "\n";
    cout << sizeof(alloc5[1]) << endl;
    printf("%d ", alloc5[2]);
    cout << "\n";
    cout << sizeof(alloc5[2]) << endl;
    printf("%d ", alloc5[3]);
    cout << "\n";
    cout << sizeof(alloc5[3]) << endl;

    free(ptr);
    free(alloc);
    free(alloc2);
    free(alloc3);
    free(alloc4);
    free(alloc5);
    return 0;
}