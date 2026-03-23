#include <iostream>

using namespace std;

class Student{
    private:
        string name;
        int age;
        double mid_grade;
    public:
        void setData(string Name, int Age, double Mid_grade)
        {
            name = Name;
            age = Age;
            mid_grade = Mid_grade;
        }
        void printInfo(){
            cout << "Имя студента: " << name << endl;
            cout << "Возраст студента: " << age << endl;
            cout << "Средний балл студента: " << mid_grade << endl;
        }
};

int main(){
    Student Borya;
    Borya.setData("Боря", 18, 4.5);
    Borya.printInfo();
}