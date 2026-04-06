#include <iostream>

using namespace std;

class Array{
    public:
        Array(){
            for(int i = 0; i < 6; i++){
                data[i] = i;
            }
        }

        int & operator[](int index){
            if (index < 0 || index > 5)
            {
                cout << "Индекс вышел за пределы массива";
                exit(1);
            }
            return data[index];
        }

    private:
        int data[5];
};

int main(){
    Array arr;

    cout << "Тест: ";
    for(int i = 0; i < 6; i++){
        cout << arr[i];
    }
    cout << endl;

    cout << arr[6];
}