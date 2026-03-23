#include <iostream>
#include <cstring>

using namespace std;

class Buffer{
    private:
        char* str;

    public:
        Buffer(const char* s){
            str = new char[strlen(s) + 1];
            strcpy(str, s);
            cout << "Конструктор вызван!" << endl;
        }

        // Правило трех
        // 1.
        Buffer(const Buffer& other){
            str = new char[strlen(other.str) + 1];
            strcpy(str, other.str);
            cout << "Копирующий конструктор вызван!" << endl;
        }

        // 2.
        Buffer& operator=(const Buffer& other){
            delete[] str;
            str = new char[strlen(other.str) + 1];
            strcpy(str, other.str);
            cout << "Копирующий оператор присваивания вызван!" << endl;
            return *this;
        }

        // 3.
        ~Buffer(){
            delete[] str;
            cout << "Деструктор вызван!" << endl;
        }

        void print(){
            cout << str << endl;
        }
};

int main() {
    Buffer b1("first");
    b1.print();

    // Проверка копирующего конструктора
    Buffer b2 = b1;
    b2.print();
    
    // Проверка копирующего оператора присваивания
    Buffer b3("third");
    b3 = b1;
    b3.print();
}