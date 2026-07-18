#include <iostream>

int main() {
  /* Be at least 8 characters
     Contain at least 1 number
     Contain at least 1 special character */
  
  bool hasValidLength = false;
  bool containsNumber = false;
  bool containsCharacter = false;
  std::string password;

  while (!containsNumber || !containsCharacter || !hasValidLength) {

    std::cout << "Enter a password: ";
    std::cin >> password;

    hasValidLength = password.length() >= 8;
    containsNumber = password.find_first_of("0123456789") != std::string::npos;
    containsCharacter = password.find_first_of("!@#%^") != std::string::npos;

    if (!hasValidLength) {
      std::cout << "❌ Password must be at least 8 characters." << std::endl;
    }
    else if (!containsNumber) {
      std::cout << "❌ Password must include a number." << std::endl;
    }
    else if (!containsCharacter) {
      std::cout << "❌ Password must include a special character." << std::endl;
    }
  }
  std::cout << "✅ Valid password!" << std::endl;
}