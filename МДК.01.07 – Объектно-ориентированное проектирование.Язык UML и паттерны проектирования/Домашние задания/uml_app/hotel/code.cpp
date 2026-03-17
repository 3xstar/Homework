#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Класс Номер
class Room {
private:
    int id;
    string type;
    double price;
    bool isBooked;

public:
    Room(int id, string t, double p) : id(id), type(t), price(p), isBooked(false) {}

    string getType() const { return type; }
    int getId() const { return id; }
    double getPrice() const { return price; }
    
    // Проверка, свободен ли номер
    bool isAvailable() const {
        return !isBooked;
    }

    // Попытка забронировать
    bool book() {
        if (!isBooked) {
            isBooked = true;
            return true;
        }
        return false;
    }

    // Отмена бронирования (для полноты функционала)
    void cancel() {
        isBooked = false;
    }

    void printInfo() const {
        cout << "Номер #" << id << " [" << type << "] - Цена: " << price << "$";
        if (isBooked) cout << " (ЗАНЯТ)";
        else cout << " (СВОБОДЕН)";
        cout << endl;
    }
};

// Класс Бронирование
class Booking {
private:
    string clientName;
    string date;
    int roomID;

public:
    Booking(string name, string d, int rId) : clientName(name), date(d), roomID(rId) {}

    void confirm() {
        cout << "\n*** ПОДТВЕРЖДЕНИЕ БРОНИРОВАНИЯ ***" << endl;
        cout << "Клиент: " << clientName << endl;
        cout << "Дата заезда: " << date << endl;
        cout << "Забронирован номер ID: " << roomID << endl;
        cout << "Ожидаем вас!" << endl;
        cout << "**********************************\n" << endl;
    }
};

// Класс Отель (Управляющая система)
class Hotel {
private:
    string name;
    vector<Room> rooms;

public:
    Hotel(string hName) : name(hName) {
        // Инициализация номеров при создании отеля
        rooms.push_back(Room(101, "Standard", 50.0));
        rooms.push_back(Room(102, "Standard", 50.0));
        rooms.push_back(Room(201, "Deluxe", 100.0));
        rooms.push_back(Room(202, "Deluxe", 100.0));
        rooms.push_back(Room(301, "Suite", 200.0));
    }

    // Метод поиска свободного номера определенного типа
    // Возвращает указатель на номер, если найден, иначе nullptr
    Room* checkAvailability(const string& type) {
        for (auto& room : rooms) {
            if (room.getType() == type && room.isAvailable()) {
                return &room;
            }
        }
        return nullptr;
    }

    // Основной метод логики задания
    bool makeBooking(const string& clientName, const string& date, const string& roomType) {
        cout << "\nПроверка наличия номеров типа '" << roomType << "' на дату " << date << "..." << endl;

        Room* availableRoom = checkAvailability(roomType);

        if (availableRoom != nullptr) {
            // Если номер найден
            if (availableRoom->book()) {
                Booking newBooking(clientName, date, availableRoom->getId());
                newBooking.confirm();
                return true;
            }
        } else {
            // Если номер не найден
            cout << "\n!!! ОТКАЗ В БРОНИРОВАНИИ !!!" << endl;
            cout << "К сожалению, номеров типа '" << roomType << "' на эту дату нет в наличии." << endl;
            cout << "Попробуйте выбрать другую дату или тип номера." << endl;
            cout << "******************************\n" << endl;
            return false;
        }
        return false;
    }

    // Показать все номера (для отладки/меню)
    void showRooms() {
        cout << "\n--- Доступные номера в отеле '" << name << "' ---" << endl;
        for (const auto& room : rooms) {
            room.printInfo();
        }
        cout << "------------------------------------------\n" << endl;
    }
};

int main() {
    Hotel myHotel("Grand Plaza");

    int choice;
    while (true) {
        cout << "=== СИСТЕМА БРОНИРОВАНИЯ ОТЕЛЯ ===" << endl;
        cout << "1. Забронировать номер" << endl;
        cout << "2. Посмотреть статус номеров" << endl;
        cout << "3. Выход" << endl;
        cout << "Выберите действие: ";
        
        if (!(cin >> choice)) {
            cin.clear();
            cin.ignore(32767, '\n');
            cout << "Ошибка ввода! Попробуйте снова.\n";
            continue;
        }

        if (choice == 3) break;

        switch (choice) {
            case 1: {
                string name, date, type;
                cout << "Введите ваше имя: ";
                cin.ignore(); // Очистка буфера после ввода числа
                getline(cin, name);

                cout << "Введите дату заезда (ДД.ММ.ГГГГ): ";
                getline(cin, date);

                cout << "Введите тип номера (Standard, Deluxe, Suite): ";
                getline(cin, type);

                // Вызов логики проверки и бронирования
                myHotel.makeBooking(name, date, type);
                break;
            }
            case 2:
                myHotel.showRooms();
                break;
            default:
                cout << "Неверный выбор.\n";
        }
    }

    cout << "Спасибо за использование системы!" << endl;
    return 0;
}