#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int an_even_numbers(vector<int>& test){
    int c = count_if(test.begin(), test.end(), [](int x){
        return x % 2 == 0;
    });
    return c;
}

int main(){
    vector<int> numbers = {1,2,3,4,5};

    cout << "Вектор: ";
    for_each(numbers.begin(), numbers.end(), [](int x){
        cout << x << " ";});
    
    cout << endl << "Количество четных чисел: " << an_even_numbers(numbers);
}