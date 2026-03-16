#include <iostream>

using namespace std;

class Car{
    public:
        string brand;

        Car(string b, int y, int s){
            brand = b;
            year = y;
            speed = s;
        }

        void setYear(int y){
           year = y;
           cout << "Year is changed!" << endl; 
        }

        void getYear(){
            cout << "Year of the car: " << year << endl;
        }

        void setSpeed(int s){
           speed = s;
           cout << "Speed is changed!" << endl; 
        }

        void getSpeed(){
            cout << "Speed of the car: " << speed << endl;
        }

        void printInfo(){
            cout << "Brand of the car: " << brand << endl;
            cout << "Year of the car: " << year << endl;
            cout << "Speed of the car: " << speed << endl;
        }

    private:
        int year;

    protected:
        int speed;
};

int main(){
    Car c1("Bugatti Lebron", 2026, 300);
    c1.printInfo();
    cout << endl;
    c1.setYear(2077);
    c1.setSpeed(500);
    cout << endl;
    c1.printInfo();
}