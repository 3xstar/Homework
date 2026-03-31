#include <iostream>

using namespace std;

class Student{
    private:
        static int count;
    
    public:
        Student(){
        count ++;
        }

        static int GetCount(){
            return count;
        }
};

int Student::count = 0;

int main(){
    Student s1;
    cout << "Count of students: " << Student::GetCount() << endl;
    Student s2;
    cout << "Count of students: " << Student::GetCount() << endl;
}