#include <iostream>
#include "math_utils.h"

using std::cout;
using std::endl;

void empty_if_for_wextra(int x){
        if(x > 0)
        {
                cout << x  << " > 0" << endl;
        }
        if(x == 0){
                cout << x  << " = 0" << endl;
        }
        if(x < 0){
                cout << x  << " < 0" << endl;
        }
}

int main(){
        int numb = 1;
        //int unused_for_wall = 100;
        empty_if_for_wextra(numb);
        cout << multiply(12, 21) << endl;
        cout << divide(24, 6) << endl;
        cout << substract(12, 32) << endl;
}