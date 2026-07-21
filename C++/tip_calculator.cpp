#include <iostream>

void tips_menu(){
  std::cout << "1) 15%\n";
  std::cout << "2) 20%\n";
  std::cout << "3) 25%\n\n";
}
double tips_calculator(double paymentTotal, int tipOption){
  if (tipOption == 1) {
    return paymentTotal * 0.15;
  }
  else if (tipOption == 2) {
    return paymentTotal * 0.2;
  }
  else if (tipOption == 3) {
    return paymentTotal * 0.25;
  }
  return 0;
}
int main() {
  int userInput = 0;
  tips_menu();
  std::cout << "You need to pay $25! Leave a Tip: ";
  std::cin >> userInput;
  std::cout << "\nYour tip is: $" << tips_calculator(25.0, userInput) << ".\n";
}