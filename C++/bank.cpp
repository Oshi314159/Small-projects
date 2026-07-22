#include <iostream>
#include <string>

class BankAccount {
  public:
    std::string name;
    int account_id;
    std::string account_type;
    double balance;

    void deposit(double amount) {
      balance += amount;
    }
    void withdraw(double amount) {
      balance -= amount;
    }
    void display_balance() {
      std::cout << "Your balance: $" << balance << std::endl;
    }
};

int main() {
  BankAccount Hyunsung;
  Hyunsung.name = "Hyunsung";
  Hyunsung.account_id = 20100908;
  Hyunsung.account_type = "Checking Account";
  Hyunsung.balance = 523;

  Hyunsung.deposit(96);
  Hyunsung.withdraw(25);
  Hyunsung.display_balance();
}