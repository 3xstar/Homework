#include <iostream>

using namespace std;

class MathUtils{
    public:
        static int add(int a, int b){
            return a + b;
        }

        static int sub(int a, int b){
            return a - b;
        }

        static int mul(int a, int b){
            return a * b;
        }
};

int main(){
    cout << "5 + 10 = " << MathUtils::add(5, 10) << endl;
    cout << "20 - 10 = " << MathUtils::sub(20, 10) << endl;
    cout << "7 * 5 = " << MathUtils::mul(7, 5) << endl;
}