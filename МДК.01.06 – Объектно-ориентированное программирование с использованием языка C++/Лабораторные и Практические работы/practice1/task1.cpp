#include <iostream>

using namespace std;

class Student{
    private:
        string name;
        int age;
        double grade;

    public:
        Student(string n, int a, double g){
            name = n;
            age = a;
            grade = g;
        }

        ~Student(){
            cout << "Student " << name << " destroyed" << endl;
        }

        void setData(){
            cout << "Enter the new name of student: ";
            cin >> name;

            cout << "Enter the new age of student: ";
            cin >> age;

            cout << "Enter the new grade of student: ";
            cin >> grade;

            cout << "Params of student changed!" << endl;
        }

        void setData(string newName, int newAge, double newGrade){
            name = newName;
            age = newAge;
            grade = newGrade;
            cout << "Params of student changed!" << endl;
        };

        void printInfo(){
            cout << "Name of student: " << name << endl;
            cout << "Age of student: " << age << endl;
            cout << "Grade of student: " << grade << endl;
        } 
};

int main(){
    Student s1("Borya", 20, 4.5);
    s1.printInfo();

    cout << endl;

    Student s2 = s1;
    s2.printInfo();

    cout << endl;
}