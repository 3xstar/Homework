#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void reverse_sort(vector<int>& test){
    sort(test.begin(), test.end(), greater<int>());
}

int main(){
    vector<int> numbers = {-5, 17, 9, 11, -2};

    cout << "Вектор: ";
    for_each(numbers.begin(), numbers.end(), [](int x){
        cout << x << " ";});
    
    cout << endl << "Вектор с сортировкой по убыванию: ";

    reverse_sort(numbers);

    for_each(numbers.begin(), numbers.end(), [](int x){
        cout << x << " ";});
}