#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    vector<int> v(15);
    iota(v.begin(), v.end(), 5);
    cout << "Заполненный вектор: ";
    for (int x : v){
        cout << x << " ";
    }

}