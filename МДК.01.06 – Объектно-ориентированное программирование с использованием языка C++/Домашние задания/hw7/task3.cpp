#include <iostream>

using namespace std;

class Product{
    public:
        string name;
        double price;

        Product(string n, double p){
            name = n;
            price = p;
            productCount++;
        }

        static int getProductCount(){
            return productCount;
        }
    
    private:
        static int productCount;
};

int Product::productCount = 0;

int main(){
    Product("Молоко", 79.9);
    cout << "Count of products: " << Product::getProductCount() << endl;
    Product("Батон", 40.0);
    cout << "Count of products: " << Product::getProductCount() << endl;
}