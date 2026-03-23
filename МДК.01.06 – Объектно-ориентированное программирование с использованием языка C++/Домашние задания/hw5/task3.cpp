#include <iostream>

using namespace std;

class Animal{
    protected:
        string name;
    
    public:
        void setName(){
            string n;
            cout << "Введите имя животного: ";
            cin >> n;
            name = n;
            cout << "Успешно! Имя животного: " << name;
        }
};

int main(){
    Animal a;
    a.setName();
}