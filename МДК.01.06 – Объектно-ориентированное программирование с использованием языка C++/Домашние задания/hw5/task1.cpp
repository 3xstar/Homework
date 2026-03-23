#include <iostream>

using namespace std;

class Car{
    private:
        string brand;
        int year;
        double speed;

    public:
        void setData(string b, int y, double s){
            brand = b;
            year = y;
            speed = s;
        }

        void printInfo(){
            cout << "Бренд машины: " << brand << endl;
            cout << "Год выпуска машины: " << year << endl;
            cout << "Средняя скорость машины: " << speed << endl;
        }
};

int main(){
    Car c;
    c.setData("Folkswagen Polo", 2000, 150);
    c.printInfo();
}