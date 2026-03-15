#include <iostream>

using namespace std;

struct Fuel{
    double amount;
    double consumption;
};

class Car{
    public:
        string model;

        Car(string m, double fuel_amount, double fuel_comsumption){
            model = m;
            fuel.amount = fuel_amount;
            fuel.consumption = fuel_comsumption;
        }

        void drive(int distance){
            double comsumption_1_km = fuel.consumption / 100;
            double wasted_fuel = comsumption_1_km * distance;
            fuel.amount -= wasted_fuel;
            cout << "Машина " << model << " проехала " << distance << " километров" << endl;
            cout << "Потраченный на путь бензин: " << wasted_fuel << " литров" << endl;
            getFuel();
        }

        void refuel(int amount){
            fuel.amount += amount;
            cout << "Бак заправлен на " << amount << " литров!" << endl;
            getFuel();
        }

        void getFuel(){
            cout << "Текущее количество бензина " << model << ": " << fuel.amount << " литров" << endl;
        }

    private:
        Fuel fuel;
};

int main(){
    Car mercedes{"Мерседес", 50, 9};
    Car bmw{"БМВ", 55, 11};
    mercedes.drive(100);
    bmw.drive(100);
}