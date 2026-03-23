#include <iostream>

using namespace std;

class Calculator{
    public:
        int add(int a, int b){
            return a + b;
        }

        int sub(int a, int b){
            return a - b;
        }

        int mul(int a, int b){
            return a * b;
        }

        double div(double a, double b){
            return a / b;
        }
};

int main(){
    Calculator c;
    cout << c.add(10, 20) << endl;
    cout << c.sub(10, 20) << endl;
    cout << c.mul(10, 20) << endl;
    cout << c.div(10, 20) << endl;
}