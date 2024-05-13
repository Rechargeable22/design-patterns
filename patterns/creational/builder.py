"""Builder is a creational design pattern that lets you construct complex objects step by
step. The pattern allows you to produce different types and representations of an object
using the same construction code."""
from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.features = {}

    def add_features(self, key, value):
        self.features[key] = value

    def __str__(self):
        return "\n".join(f"{key}: {value}" for key, value in self.features.items())


class CarBuilder(ABC):
    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_wheels(self):
        pass

    @abstractmethod
    def build_gps(self):
        pass

    @abstractmethod
    def get_car(self):
        pass


class MyCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.add_features("engine", "v8")

    def build_wheels(self):
        self.car.add_features("wheels", "really big")

    def build_gps(self):
        self.car.add_features("gps", "super garmin gps")

    def get_car(self):
        return self.car


class Director:
    def __init__(self, builder):
        self._builder = builder

    def construct_sports_car(self):
        self._builder.build_engine()
        self._builder.build_wheels()
        self._builder.build_gps()
        return self._builder.get_car()


if __name__ == '__main__':
    builder = MyCarBuilder()
    director = Director(builder)

    sports_car = director.construct_sports_car()
    print(sports_car)

    """In Python we can use named parameters for this."""
