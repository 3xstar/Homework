#include <iostream>

using namespace std;

class Product{
    private:
        string name;
        double price;
        int quantity;

    public:
        Product(string n, double p, int q){
            name = n;
            price = p;
            quantity = q;
        }

        void printInfo(){
            cout << "Name of the product: " << name << endl;
            cout << "Price of the product: " << price << endl;
            cout << "Quantity of the product: " << quantity << endl;
        }

        void buy(int amount){
            if(quantity < 1){
                cout << "There is no product in stock";
            }
            else{
                if(amount <= quantity){
                    quantity -= amount;
                    cout << name << " buyed in quantity of " << amount << endl;
                }
                else{
                    cout << "Amount cant be bigger than quantity of product in stock" << endl;
                }
            }
        }

        void setData(){
            cout << "Enter the new name of product: ";
            cin >> name;

            cout << "Enter the new price of product: ";
            cin >> price;

            cout << "Enter the new quantity of product: ";
            cin >> quantity;

            cout << "Params of product changed!" << endl;
        }

        void setData(string newName, int newPrice, double newQuantity){
            this -> name = newName;
            this -> price = newPrice;
            this -> quantity = newQuantity;
            cout << "Params of product changed!" << endl;
        };
};

int main(){
    Product p1("Computer", 10000.0, 20);
    p1.printInfo();
    cout << endl;
    p1.buy(3);
    cout << endl;
    p1.printInfo();
}