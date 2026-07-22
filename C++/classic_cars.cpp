#include <iostream>
#include <string>

class Car {
    public:
        std::string brand = "";
        std::string model = "";
        int year = 0;
        bool classic = false;

        Car(std::string b, std::string m, int y, bool c) {
            brand = b;
            model = m;
            year = y;
            classic = c;
        }
        void displayCar() {
            std::cout << "Brand: " << brand << std::endl;
            std::cout << "Model: " << model << std::endl;
            std::cout << "Year: " << year << std::endl;
            if (classic == true) {
                std::cout << "Classic" << std::endl;
            }
            else {
                std::cout << "Not classic" << std::endl;
            }
        }
};

int main() {
    Car myCar("Ford", "Mustang", 1961, true);
    myCar.displayCar();
}