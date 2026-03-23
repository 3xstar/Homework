#include <iostream>
#include <cstring>

using namespace std;

class String{
    private:
        char* str;

    public:
        String(const char* s){
            str = new char[strlen(s) + 1];
            strcpy(str, s);
            cout << "Конструктор вызван!" << endl;
        }

        String(const String& other){
            str = new char[strlen(other.str) + 1];
            strcpy(str, other.str);
            cout << "Копирующий конструктор вызван!" << endl;
        }

        String& operator=(const String& other){
            delete[] str;
            str = new char[strlen(other.str) + 1];
            strcpy(str, other.str);
            cout << "Оператор присваивания вызван!" << endl;
            return *this;
        }

        ~String(){
            delete[] str;
            cout << "Деструктор вызван!" << endl;
        }

        void print(){
            cout << str << endl;
        }
};

int main() {
    String s1("Hello");
    s1.print();

    String s2 = s1;
    s2.print();

    String s3("World");
    s3 = s1;
    s3.print();
}