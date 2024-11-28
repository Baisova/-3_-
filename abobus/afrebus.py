
from abc import ABC, abstractmethod

class TravelStrategy(ABC):
    @abstractmethod
    def travel(self, transportName, destination): 
        pass

class BusTravel(TravelStrategy):
    def travel(self, transportName, destination):
        print(f"Еду на автобусе: {transportName} до {destination}")

class AirplaneTravel(TravelStrategy):
    def travel(self, transportName, destination):
        print(f"Лечу на самолёте: {transportName} до {destination}")

class TrainTravel(TravelStrategy):
    def travel(self, transportName, destination):
        print(f"Еду на поезде: {transportName} до {destination}")

class ShipTravel(TravelStrategy):
    def travel(self, transportName, destination):
        print(f"Плыву на корабле: {transportName} до {destination}")

class TravelAgency:
    def __init__(self, strategy: TravelStrategy):  
        self.strategy = strategy

    def set_strategy(self, strategy: TravelStrategy):
        self.strategy = strategy

    def plan_trip(self, transportName, destination):
        self.strategy.travel(transportName, destination)

bus_travel = BusTravel()
airplane_travel = AirplaneTravel()
train_travel = TrainTravel()
ship_travel = ShipTravel()

agency = TravelAgency(bus_travel)
agency.plan_trip("Двухэтажный", "Москва")

agency.set_strategy(airplane_travel)
agency.plan_trip("Sukhoi Superjet", "Токио")

agency.set_strategy(train_travel)
agency.plan_trip("Экспресс", "Санкт-Петербург")

agency.set_strategy(ship_travel)
agency.plan_trip("Круизный лайнер", "Сочи")