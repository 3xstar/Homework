#include <iostream>

using namespace std;

class Rectangle{
    private:
        double width;
        double height;

    public:
        void setSize(int w, int h){
            width = w;
            height = h;
        }

        double area(){
            return width * height;
        }

        double perimeter(){
            return (width * 2) + (height * 2);
        }
};

int main(){
    Rectangle r;
    r.setSize(10, 20);
    cout << r.area() << endl;
    cout << r.perimeter() << endl;
}