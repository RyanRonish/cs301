class Computer:
    def __init__(self, brand, model, storage, features):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.features = features

    def start(self):
        return f"This is the new {self.brand}. => {self.model}."
    
class Apple(Computer):
    def __init__(self, brand, model, storage, features='apple_ceo'):
        super().__init__(brand, model, storage, features)
        self.features = features

    def macbook(self):
        return f"I am the new {self.features} macbook."
        
class Microsoft(Computer):
    def __init__(self, brand, model, storage, features='microsoft_ceo'):
        super().__init__(brand, model, storage, features)
        self.features = features

    def surface(self):
        return f"I am the new {self.features} surface."
    
class Lenovo(Computer):
    def __init__(self, brand, model, storage, features='lenovo_ceo'):
        super().__init__(brand, model, storage, features)
        self.features = features

    def yoga(self):
        return f"I am the new {self.features} Yoga."
    

apple_ceo = Apple("APPLE", "M3", "3TB", "Touchscreen")
microsoft_ceo = Microsoft("Microsoft", "Surface", "1TB", "QLED")
lenovo_ceo = Lenovo("LENovo", "YOGA", "512GB", "Antivirus")

print(apple_ceo.start())
print(apple_ceo.macbook())

print(microsoft_ceo.start())
print(microsoft_ceo.surface())

print(lenovo_ceo.start())
print(lenovo_ceo.yoga())