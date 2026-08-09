class Pokemon:
    def __init__(self, entry, name, type, description, is_caught):
        self.entry = entry
        self.name = name
        self.type = type
        self.description = description
        self.is_caught = is_caught
        
    def speak(self):
        print(f"{self.name}, {self.name}!")
        
    def display_details(self):
        print(f"Entry Number: {self.entry}")
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Description: {self.description}")
        
pikachu = Pokemon(25, "Pikachu", "Electric", "It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs. Pikachu has already been caught!", True)
pikachu.speak()
pikachu.display_details()