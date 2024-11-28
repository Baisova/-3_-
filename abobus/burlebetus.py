from abc import ABC, abstractmethod

class Computer:
    def __init__(self, cpu=None, ram=None, storage=None, gpu=None, components=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.components = components

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}, Components: {self.components}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_components(self, components):
        self.computer.components = components
        return self

    def build(self):
        return self.computer

class Animal(ABC):
    def __init__(self, behavior):
        self.behavior = behavior

    def perform_behavior(self):
        self.behavior.behave()

class Behavior(ABC):
    @abstractmethod
    def behave(self):
        pass

class MeowStrategy(Behavior):
    def behave(self):
        print("Мяукаю!")

class FlyStrategy(Behavior):
    def behave(self):
        print("Лечу!")

class Cat(Animal):
    def __init__(self, behavior):
        super().__init__(behavior)

class Bird(Animal):
    def __init__(self, behavior):
        super().__init__(behavior)

builder = ComputerBuilder()
computer = (builder.set_cpu("Intel i9")
            .set_ram("16GB")
            .set_storage("1TB SSD")
            .set_gpu("NVIDIA RTX 3080")
            .set_components("Cooling System")
            .build())
print("Созданный компьютер:")
print(computer)

cat = Cat(MeowStrategy())
bird = Bird(FlyStrategy())

print("\nЖивотные с поведением:")
cat.perform_behavior() # Мяукаю!
bird.perform_behavior() # Лечу!