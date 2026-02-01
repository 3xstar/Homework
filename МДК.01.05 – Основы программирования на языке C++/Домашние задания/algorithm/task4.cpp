#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> min_element_zero(vector<int>& test){
    auto min = min_element(test.begin(), test.end());
    int min_value = *min; 

    transform(test.begin(), test.end(), test.begin(), [min_value](int x){
        return (x == min_value) ? 0 : x;
    });

    return test;
}

int main(){
    vector<int> numbers = {1,2,3,4,5};

    cout << "Вектор: ";
    for_each(numbers.begin(), numbers.end(), [](int x){
        cout << x << " ";});
    
    cout << endl << "Вектор с заменой минимального элемента на 0: ";

    numbers = min_element_zero(numbers);

    for_each(numbers.begin(), numbers.end(), [](int x){
        cout << x << " ";});
}