#include <iostream>

using namespace std;

class BankAccount{
    private:
        int account_number;
        string owner;
        double balance = 0;

    public:
        void deposit(){
            double amount; 
            cout << "Введите сумму депозита: ";
            cin >> amount;
            if(amount > 0){
                balance += amount;
                cout << "Вы внесли депозит! Нынешний баланс: " << balance << endl;
            }
            else{
                cout << "Вы не можете внести депозит равный 0 или меньше" << endl;
                return;
            }
        }

        void withdraw(){
            double amount; 
            cout << "Введите сумму снятия: ";
            cin >> amount;
            if(amount <= balance){
                balance -= amount;
                cout << "Вы сняли деньги! Нынешний баланс: " << balance << endl;
            }
            else{
                cout << "Вы не можете снять с депозита больше, чем есть на балансе" << endl;
                return;
            }
        }

        void getBalance(){
            cout << "Ваш текущий баланс: " << balance << endl;
        }
};

int main(){
    BankAccount BA;
    BA.getBalance();
    BA.deposit();
    BA.withdraw();
}