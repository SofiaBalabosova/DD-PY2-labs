if __name__ == "__main__":
    class Car:
        """
        Базовый класс Car, представляющий общий интерфейс для всех автомобилей.
        """

        def __init__(self, make: str, model: str, year: int) -> None:
            """
            Конструктор для инициализации автомобиля.

            :param make: Производитель автомобиля.
            :param model: Модель автомобиля.
            :param year: Год выпуска автомобиля.
            Приватные атрибуты, так как не должны меняться извне
            """
            self._make = make  # Производитель (приватный атрибут)
            self._model = model  # Модель (приватный атрибут)
            self._year = year  # Год выпуска (приватный атрибут)

        def __str__(self) -> str:
            """
            Возвращает строковое представление автомобиля.
            """
            return f"Автомобиль {self._make} {self._model}"

        def __repr__(self) -> str:
            """
            Возвращает формальное представление автомобиля.
            """
            return f"{self.__class__.__name__}(make='{self._make!r}', model='{self._model!r}', year={self._year!r})"

        def start_engine(self) -> str:
            """
            Запускает двигатель автомобиля.

            :return: Строка с сообщением о запуске двигателя.
            """
            return f"The engine of {self} is starting."

        def honk_horn(self) -> str:
            """
            Издает сигнал автомобилем.

            :return: Строка с сообщением о звуке сигнала.
            """
            return f"{self._make} {self._model} goes 'Beep beep!'"


    class Sedan(Car):
        """
        Класс Sedan, представляющий легковой автомобиль.
        """

        def __init__(self, make: str, model: str, year: int, passenger_capacity: int) -> None:
            """
            Конструктор для инициализации легкового автомобиля.

            :param make: Производитель легкового автомобиля.
            :param model: Модель легкового автомобиля.
            :param year: Год выпуска легкового автомобиля.
            :param passenger_capacity: Вместимость пассажиров.
            """
            super().__init__(make, model, year)  # Вызов конструктора базового класса
            self.__passenger_capacity = passenger_capacity  # Вместимость пассажиров (приватный атрибут)

        def __repr__(self) -> str:
            """
            Возвращает формальное представление автомобиля.
            """
            return (f"{self.__class__.__name__}(make='{self._make!r}', model='{self._model!r}', year={self._year!r}, "
                    f"passenger_capacity={self.__passenger_capacity!r})")

        def start_engine(self) -> str:
            """
            Запускает двигатель легкового автомобиля.

            Переопределенный метод, чтобы добавить информацию о бесшумности двигателя легкового автомобиля.
            """
            return f"The engine of {self} is starting silently!"


    class Truck(Car):
        """
        Класс Truck, представляющий грузовой автомобиль.
        """

        def __init__(self, make: str, model: str, year: int, load_capacity: float) -> None:
            """
            Конструктор для инициализации грузового автомобиля.

            :param make: Производитель грузового автомобиля.
            :param model: Модель грузового автомобиля.
            :param year: Год выпуска грузового автомобиля.
            :param load_capacity: Грузоподъемность автомобиля.
            """
            super().__init__(make, model, year)  # Вызов конструктора базового класса
            self.__load_capacity = load_capacity  # Грузоподъемность (приватный атрибут)

        def __repr__(self) -> str:
            """
            Возвращает формальное представление автомобиля.
            """
            return (f"{self.__class__.__name__}(make='{self._make!r}', model='{self._model!r}', year={self._year!r}, "
                    f"load_capacity={self.__load_capacity!r})")

        def start_engine(self) -> str:
            """
            Запускает двигатель грузового автомобиля.

            Переопределенный метод, чтобы добавить информацию о мощности двигателя грузовика.
            """
            return f"The powerful engine of {self} is starting with a roar!"



    # Write your solution here
    pass
