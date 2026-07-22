#include <iostream>
#include <string>

class Cat {
public:
    std::string name;
    bool breed = false;
    int age;
    bool rescued;
    int mood;
    int hunger;

    Cat(std::string n, bool b, int a, bool r, int m, int h) {
        name = n;
        breed = b;
        age = a;
        rescued = r;
        mood = m;
        hunger = h;
    }

    void feed() {
        if (hunger > 0) {
            hunger -= 1;
        }
        std::cout << name << "'s hunger was decreased by 1!" << std::endl;
    }

    void play() {
        mood += 1;
        std::cout << name << "'s mood was increased by 1!" << std::endl;
    }

    void status() {
        std::cout << "Name: " << name << std::endl;
        std::cout << "Breed: " << (breed ? "Yes" : "No") << std::endl;
        std::cout << "Age: " << age << std::endl;
        std::cout << "Rescued: " << (rescued ? "Yes" : "No") << std::endl;
        std::cout << "Mood: " << mood << std::endl;
        std::cout << "Hunger: " << hunger << std::endl;
    }
};

int main() {
    bool online = true;
    Cat Kit("Kit", false, 5, true, 5, 2);
    Cat Jade("Jade", true, 8, true, 7, 1);

    std::string action = "";
    while (online) {
        std::cout << "1) Feed" << std::endl;
        std::cout << "2) Play" << std::endl;
        std::cout << "3) Check Status" << std::endl;
        std::cout << "4) Quit" << std::endl;
        std::cout << "Choose an action: ";
        std::cin >> action;

        if (action == "1" || action == "Feed") {
            std::cout << "Kit or Jade?" << std::endl;
            std::cin >> action;
            if (action == "Kit") {
                Kit.feed();
            } else if (action == "Jade") {
                Jade.feed();
            } else {
                std::cout << "Invalid answer!" << std::endl;
            }
        } else if (action == "2" || action == "Play") {
            std::cout << "Kit or Jade?" << std::endl;
            std::cin >> action;
            if (action == "Kit") {
                Kit.play();
            } else if (action == "Jade") {
                Jade.play();
            } else {
                std::cout << "Invalid answer!" << std::endl;
            }
        } else if (action == "3" || action == "Check") {
            std::cout << "Kit or Jade?" << std::endl;
            std::cin >> action;
            if (action == "Kit") {
                Kit.status();
            } else if (action == "Jade") {
                Jade.status();
            } else {
                std::cout << "Invalid answer!" << std::endl;
            }
        } else if (action == "4" || action == "Quit") {
            std::cout << "See you later!" << std::endl;
            online = false;
        } else {
            std::cout << "Invalid answer!" << std::endl;
        }
    }

    return 0;
}
