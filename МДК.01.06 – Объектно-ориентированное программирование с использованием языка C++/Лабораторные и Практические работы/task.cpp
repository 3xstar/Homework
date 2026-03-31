#include <iostream>

using namespace std;

class Fraction{
    private:
        int numerator;
        int denominator;
    
    public:
        Fraction(){
            numerator = 0;
            denominator = 1;
        }

        Fraction(int n, int d){
            if(d == 0){
                cout << "Error: The denominator cannot be zero" << endl;
                numerator = 0;
                denominator = 1;
            }
            else{
                numerator = n;
                denominator = d;
                simplify();
            }
        }

        void print() const{
            cout << numerator << " / " << denominator;
        }

        Fraction operator+(const Fraction& other) const{
            int new_numerator = this->numerator * other.denominator + other.numerator * this->denominator;
            int new_denominator = this->denominator * other.denominator;

            return Fraction(new_numerator, new_denominator);
        }

        Fraction operator-(const Fraction& other) const{
            int new_numerator = this->numerator * other.denominator - other.numerator * this->denominator;
            int new_denominator = this->denominator * other.denominator;

            return Fraction(new_numerator, new_denominator);
        }

        Fraction operator*(const Fraction& other) const{
            int new_numerator = this->numerator * other.numerator;
            int new_denominator = this->denominator * other.denominator;

            return Fraction(new_numerator, new_denominator);
        }

        Fraction operator/(const Fraction& other) const{
            int new_numerator = this->numerator * other.denominator;
            int new_denominator = this->denominator * other.numerator;

            return Fraction(new_numerator, new_denominator);
        }

        bool operator==(const Fraction& other) const{
            int new_numerator = this->numerator * other.denominator;
            int new_denominator = other.numerator * this->denominator;

            return new_numerator == new_denominator;
        }

        friend ostream& operator<<(ostream& os, const Fraction& f) {
            os << f.numerator << " / " << f.denominator;
            return os;
        }

        void simplify() {
            int a = numerator;
            int b = denominator;

            if (a < 0) a = -a;
            if (b < 0) b = -b;


            while (b != 0) {
                int temp = b;
                b = a % b;
                a = temp;
            }

            if (a == 0) return; 

            numerator /= a;
            denominator /= a;

            if (denominator < 0) {
                numerator = -numerator;
                denominator = -denominator;
            }
            
            if (numerator == 0) {
                denominator = 1;
            }
        }
};

int main(){
    Fraction f1;
    Fraction f2(1, 2);
    Fraction f3(3, 4);
    Fraction f4(2, 4);
    Fraction f5(0, 5);
    Fraction f6(5, 0); 
    Fraction f7(-3, -6);
    Fraction f8(5, -10);

    cout << "Default constructor: ";
    cout << f1 << endl;

    cout << "Constructor with params: ";
    cout << f2 << endl;

    cout << "Error handling (denom=0): ";
    cout << f6 << endl;

    cout << "Print method: ";
    f3.print();
    cout << endl;

    cout << "Addition (1/2 + 3/4): ";
    cout << f2 + f3 << endl;

    cout << "Subtraction (1/2 - 3/4): ";
    cout << f2 - f3 << endl;

    cout << "Multiplication (1/2 * 3/4): ";
    cout << f2 * f3 << endl;

    cout << "Division (1/2 / 3/4): ";
    cout << f2 / f3 << endl;

    cout << "Equality (1/2 == 2/4): ";
    if (f2 == f4) {
        cout << "Equal" << endl;
    } else {
        cout << "Not equal" << endl;
    }

    cout << "Equality (1/2 == 3/4): ";
    if (f2 == f3) {
        cout << "Equal" << endl;
    } else {
        cout << "Not equal" << endl;
    }

    cout << "Simplify test (2/4): ";
    cout << f4 << endl;

    cout << "Negative simplify (-3/-6): ";
    cout << f7 << endl;

    cout << "Negative simplify (5/-10): ";
    cout << f8 << endl;

    cout << "Zero numerator (0/5): ";
    cout << f5 << endl;

    return 0;
}