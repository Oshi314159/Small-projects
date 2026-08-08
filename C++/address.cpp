#include <iostream>

void reviewAction(const std::string& name, const std::string* extraComment) {
    if (extraComment != nullptr && name != "") {
        std::cout << "Thanks for the review, " << name << "! The team will get back to you if you had any questions."
                << std::endl;
        return;
    }
    if (name != "") {
        std::cout << "Thanks for the review, " << name << "!" << std::endl;
        return;
    }
    return;
}

int main() {
    reviewAction("", nullptr);
}