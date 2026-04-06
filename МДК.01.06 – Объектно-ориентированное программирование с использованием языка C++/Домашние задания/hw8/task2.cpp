#include <iostream>

using namespace std;

class Count{
    public:
        Count(int v) : value(v){}

        // префиксный
        Count& operator++(){
            value++;
            return *this;
        }

        // постфиксный
        Count& operator++(int){
            Count temp = *this;
            value++;
            return temp;
        }

        // префиксный
        Count& operator--(){
            value--;
            return *this;
        }

        // постфиксный
        Count& operator--(int){
            Count temp = *this;
            value++;
            return temp;
        }

    private:
        int value;
};

int main(){
    Count counter(10);
    ++counter;
    counter++;
    --counter;
    counter--;
}