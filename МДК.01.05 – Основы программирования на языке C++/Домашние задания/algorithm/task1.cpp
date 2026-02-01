#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int less_than_zero(vector<int>& test){
    int c = count_if(test.begin(), test.end(), [](int x){
        return x < 0;});
    return c;
}

int main(){
    vector<int> numbers = {-5,-4,-3,-2,-1, 0, 1,2,3,4,5};

    cout << "Вектор: ";
    for_each(numbers.begin(), numbers.end(), [](int x){
        cout << x << " ";});
    
    cout << endl << "Количество отрицательных чисел: " << less_than_zero(numbers);
}