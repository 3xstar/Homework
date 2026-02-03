#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    vector <int> v = {9, 4, 8, 6, 2, 5, 7, 10, 3, 1};

    int sum = accumulate(v.begin(), v.end(), 0);
    cout << "Сумма всех элементов вектора v = " << sum << endl;

    int composition = accumulate(v.begin(), v.end(), 1, [](int a, int b){
        return a * b;}
    );

    cout << "Сумма произведения вектора v: " << composition;

}