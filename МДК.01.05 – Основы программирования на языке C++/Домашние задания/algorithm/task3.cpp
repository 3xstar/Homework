#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

auto positive_check(vector<int>& test){
    auto it = find_if(test.begin(), test.end(), [](int x){
        return x < 1;
    });
    return it;
}

int main(){
    vector<int> numbers = {-1, 1,2,3,4,5};

    cout << "Вектор: ";
    for_each(numbers.begin(), numbers.end(), [](int x){
        cout << x << " ";});

    cout << endl << "Условие: все элементы массива положительные" << endl << "Результат проверки: ";

    auto it = positive_check(numbers);
    if(it == numbers.end()){
        cout << "положительный";
    }
    else{
        cout << "отрицательные числа обнаружены: " << *it;
    }
}