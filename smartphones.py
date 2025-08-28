# Smartphone base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
    
    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")
    
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB")

# Inherited class with polymorphism
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)  # Call parent constructor
        self.cooling_system = cooling_system
    
    # Overriding method
    def info(self):
        print(f"Gaming Phone - {self.brand} {self.model}, {self.storage}GB, Cooling: {self.cooling_system}")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256)
phone2 = GamingPhone("Asus", "ROG Phone 7", 512, "Liquid Cooling")

# Use methods
phone1.info()
phone1.call("123456789")

phone2.info()
phone2.call("987654321")
