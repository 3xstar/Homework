#include <iostream>

using namespace std;

class Point{
    public:
        Point(int x, int y){
            this-> x=x;
            this-> y=y;
        }

        Point operator+(const Point& other){
            return Point(x + other.x, y + other.y);
        }
        Point operator-(const Point& other){
            return Point(x-other.x, y-other.y);
        }

        bool operator==(const Point& other){
            return x == other.x && y == other.y;
        }

        void display(){
            cout << "(" << x << "," << y << ")" << endl;
        }

    private:
        int x,y;
};

int main(){
    Point point1(2,3);
    Point point2(5,6);

    Point point3 = point1 + point2;
    point3.display();

    Point point4 = point1 + point2;
    point4.display();

    if(point1==point2){
        cout << "Координаты равны" << endl;
    }
    else{
        cout << "Координаты не равны" << endl;
    }
}