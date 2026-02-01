#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

void reverse_sort(vector<string>& test){
    sort(test.begin(), test.end(), greater<string>());
}

int main(){
    vector<string> words = {"Apple", "Computer", "Zahar", "School"};

    cout << "Вектор: ";
    for_each(words.begin(), words.end(), [](string x){
        cout << x << " ";});
    
    cout << endl << "Вектор с сортировкой по обратному алфавиту: ";

    reverse_sort(words);

    for_each(words.begin(), words.end(), [](string x){
        cout << x << " ";});
}