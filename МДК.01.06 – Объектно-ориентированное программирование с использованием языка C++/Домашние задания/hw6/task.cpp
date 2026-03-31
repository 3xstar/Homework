#include <iostream>

using namespace std;

enum category{coat, jacket, raincoat, hoodie, windbreaker};
string categoryToString(category cat) {
    switch (cat) {
        case coat: return "coat";
        case jacket: return "jacket";
        case raincoat: return "raincoat";
        case hoodie: return "hoodie";
        case windbreaker: return "windbreaker";
        default: return "unknown";
    }
}


class Clothes{
    private:
        category type;
        string name;
        double price;
        string size;
        string color;
    
    public:
        Clothes(category t, string n, double p, string s, string c){
            type = t;
            name = n;
            price = p;
            size = s;
            color = c;
        }

        string getName(){
            return name;
        }
        void setName(string new_name){
            name = new_name;
        }

        double getPrice(){
            return price;
        }
        void setPrice(double new_price){
            price = new_price;
        }

        auto getCategory(){
            return type;
        }
        void setCategory(category new_category){
            type = new_category;
        }
};

int main(){
    Clothes cool_coat(coat, "Крутое пальто", 4999.99, "XXL", "Черный");
    cout << "Название одежды: " << cool_coat.getName() << endl;
    cout << "Смена названия..." << endl;
    cool_coat.setName("Супер крутое пальто");
    cout << "Новое название одежды: " << cool_coat.getName() << endl;

    cout << "\n";

    cout << "Цена одежды: " << cool_coat.getPrice() << endl;
    cout << "Смена цены..." << endl;
    cool_coat.setPrice(9999.99);
    cout << "Новая цена одежды: " << cool_coat.getPrice() << endl;

    cout << "\n";

    cout << "Категория одежды: " << categoryToString(cool_coat.getCategory()) << endl;
    cout << "Смена категории..." << endl;
    cool_coat.setCategory(jacket);
    cout << "Новая категория одежды: " << categoryToString(cool_coat.getCategory()) << endl;
}