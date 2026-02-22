// Инвентарь

/*
Данное приложение предназначено для простого взаимодействия с RPG-инвентарем:
1. Просмотр инвентаря;
2. Фильтрация данных внутри инвентаря.
*/

/*
Из чего состоит инвентарь:
- Предметы со следующими характеристиками:
        - Редкость предмета;
        - Стоимость предмета;
        - Тип предмета;
        - Вес предмета.
*/

#include <iostream>
#include <vector>

using namespace std;

enum ItemType{
        armor,
        weapon,
        potion,
        other
};

enum Rarity{
        usually,
        rare,
        epic,
        legenagary  
};

/// Распаковка типа предмета
string typeToString(ItemType type){
        switch(type){
                case armor: return "Броня";
                case weapon: return "Оружие";
                case potion: return "Зелье";
                case other: return "Другое"; 
        }
        return "Такого типа не существует";
};

// Распаковка редкости предмета
string rarityToString(Rarity rarity){
        switch(rarity){
                case usually: return "Обычная";
                case rare: return "Редкая";
                case epic: return "Эпическая";
                case other: return "Особая"; 
        }
        return "Такой редкости не существует";
};


struct Item{
        int id;
        string name;
        ItemType type;
        Rarity rarity;
        int value;
        double weight;
};

// Получение текущей вместимости инвенторя
double getTotalWeight(const vector<Item>&inventory){
        double total = 0;
        for (const auto& item : inventory){
                total += item.weight;
        }
        return total;
};

void listItems(const vector<Item> & inventory, double maxWeigth){
        for(const auto &item : inventory){
                cout << item.id << " | " << item.name << " | "
                << typeToString(item.type) << " | " << rarityToString(item.rarity) << " | " << item.value << " | " << item.weight << endl;
        }
}

// Добавление предмета в инвентарь
bool addItem(vector<Item> &inventory, const Item &item, const double &maxWeight){
        if(getTotalWeight(inventory) + item.weight > maxWeight){
                cout << "Инвентарь переполнен!!!";
                return false;
        }
        inventory.push_back(item);
        cout << "Предмет успешно добавлен" << endl;
        return true;
};

void searchItem(const vector<Item>&inventory){
    int search_id;
    cout << "Введите ID игрового предмета для поиска: ";
    cin >> search_id;
    bool found = false;
    for(const auto &i : inventory){
        if(i.id == search_id){
            cout << "Предмет найден!\n";
            cout << "Информация о предмете:\n";
            cout << "ID предмета - " << i.id << "\nНазвание предмета - " << i.name << "\nТип предмета - " << typeToString(i.type) << 
            "\nРедкость предмета - " << rarityToString(i.rarity) << "\nЦенность предмета - " << i.value << "\nВес предмета - " << i.weight << "\n";
            found = true;
            break;
        }
    }
    if(!found){
        cout << "Предмет по ID - " << search_id << " не найден\n";
    }
}

void deleteItem(vector<Item>&inventory){
    int search_id;
    cout << "Введите ID игрового предмета для удаления: ";
    cin >> search_id;
    bool found = false;
    for(int i = 0; i < inventory.size(); i++){
        if(inventory[i].id == search_id){
            string itemName = inventory[i].name;
            inventory.erase(inventory.begin() + i);
            cout << "Предмет " << itemName << " успешно удален!";
            found = true;
            break;
        }
    }
    if(!found){
        cout << "Предмет по ID - " << search_id << " не найден\n";
    }
}

int main(){

        cout << endl;
        vector<Item> inventory;
        double maxWeight = 100.0;

        // Создаем предметы
        Item sword = {1, "Стальной меч", weapon, usually, 50, 5.0};
        Item dragonArmor = {2, "Драконья броня", armor, epic, 2500, 52.0};
        Item healthPotion = {3, "Лечебное зелье", potion, rare, 200, 1.0};
        
        addItem(inventory, sword, maxWeight);
        addItem(inventory, dragonArmor, maxWeight);
        addItem(inventory, healthPotion, maxWeight);

        listItems(inventory, maxWeight);
        searchItem(inventory);
        deleteItem(inventory);
        cout << "\n";
        listItems(inventory, maxWeight);
}