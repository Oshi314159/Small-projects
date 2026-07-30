#include <iostream>
#include <vector>

std::string convert(std::string message, int number) {
    for (char &c : message) {
        if (c >= 'a' && c <= 'z') {
            c = (c - 'a' + number) % 26 + 'a';
        }
        else if (c >= 'A' && c <= 'Z') {
            c = (c - 'A' + number) % 26 + 'A';
        }
    }

    return message;
}

int main() {
    std::string message;
    int secretNumber;

    std::cout << "Enter your message: ";
    std::cin >> message;
    std::cout << "Enter your secret number: ";
    std::cin >> secretNumber;

    std::cout << convert(message, secretNumber) << std::endl;
}