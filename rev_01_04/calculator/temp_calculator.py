from abc import ABC, abstractmethod


class TemperatureCalculatorInterface(ABC):

    @abstractmethod
    def celsius_to_farenheit(self, temp: float) -> float:
        raise NotImplementedError

    @abstractmethod
    def farenheit_to_celsius(self, temp: float) -> float:
        raise NotImplementedError

    @abstractmethod
    def convert_temp(self, temp: float, initial: str, target: str) -> float:
        raise NotImplementedError


class TemperatureCalculator(TemperatureCalculatorInterface):
    pass