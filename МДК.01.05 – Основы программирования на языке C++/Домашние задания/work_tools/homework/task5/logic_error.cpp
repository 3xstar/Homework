#include <iostream>

using std::cout;
using std::endl;

int find_max(int arr[], int size){
    int max = arr[0];
    for(int i = 0; i < size; i++)
    {
        if(arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}

int main(){
    int test_arr[] = {2,1,3,5,4};
    find_max(test_arr, 5);
}