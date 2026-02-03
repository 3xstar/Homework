#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main(){
    vector<int> v = {11,7,24,50,9};
    for_each(v.begin(), v.end(), [](int x){
        cout << x << " ";
    });

    auto count = count_if(v.begin(), v.end(), [](int x){
        return x > 10;
    });

    cout << "\nКоличество чисел больше 10 в векторе: " << count;
}