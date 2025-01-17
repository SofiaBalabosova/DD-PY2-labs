# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Barrel:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Бочка
        :param capacity_volume: Объем бочки
        :param occupied_volume: Объем занимаемой жидкости
        Примеры:
        >>> barrel = Barrel(500, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем должен быть положительным числом")
        self.capacity_volume = capacity_volume  # объем бочки
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # занятый объем бочки

    def is_full_barrel(self) -> bool:
        """
        Функция которая проверяет является ли бочка полной

        :return: Является ли бочка полной

        Примеры:
        >>> barrel = Barrel(500, 0)
        >>> barrel.is_full_barrel()
        """
    def add_water_to_barrel(self, water: float) -> None:
        """
        Добавление воды в бочку.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бочке, то вызываем ошибку

        Примеры:
        >>> barrel = Barrel(500, 0)
        >>> barrel.add_water_to_barrel(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна быть положительным числом")


class Table:
    def __init__(self, material: str):
        """
        Создание и подготовка к работе объекта Стол
        :param material: Материал стола
        :param height: Высота стола
        Примеры:
        >>> table = Table('Дуб')  # инициализация экземпляра класса
        """
        self.material = material
        self.height = []    # создание пустого списка для высоты стола

    def add_height(self, height: str) -> None:
        """
        Добавление высоты стола.
        :param height: высота
        Примеры:
        >>> table = Table('Дуб')
        >>> table.add_height('120 см')
        """

    def check_height(self, height: str) -> bool:
        """
        Функция, которая проверяет, есть ли нужная высота стола

        :return: Есть ли стол нужной высоты

        Примеры:
        >>> table = Table('Дуб')
        >>> table.check_height('100 см')
        """


class Flashdrive:
    def __init__(self, files: str, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта Флешка
        :param files: вид файлов на флешке
        :param capacity_volume: объем памяти на флешке
        :param occupied_volume: объем файлов на флешке
        Примеры:
        >>> flashdrive = Flashdrive('картинки',128, 0)  # инициализация экземпляра класса
        """
        self.files = files    # вид файлов на флешке
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем памяти на флешке должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем памяти на флешке должен быть положительным числом")
        self.capacity_volume = capacity_volume  # объем памяти на флешке
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем файлов на флешке должен быть int или float")
        if occupied_volume < 0:
            raise ValueError("Объем файлов на флешке не может быть отрицательным числом")
        self.occupied_volume = occupied_volume  # объем файлов на флешке

    def is_empty_flashdrive(self) -> bool:
        """
        Функция которая проверяет является ли флешка пустой

        :return: Является ли флешка пустой

        Примеры:
        >>> flashdrive = Flashdrive('картинки',128, 0)
        >>> flashdrive.is_empty_flashdrive()
        """
    def add_files_to_flashdrive(self, new_file: str, volume: Union[int, float]) -> None:
        """
        Заполнение флешки.
        :param new_file: тип файла

        :raise ValueError: Если объем добавляемых файлов превышает свободное место на флешке, то вызываем ошибку

        Примеры:
        >>> flashdrive = Flashdrive('картинки',128, 0)
        >>> flashdrive.add_files_to_flashdrive('картинки', 16)
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем добавляемых файлов должен быть типа int или float")
        if volume < 0:
            raise ValueError("Объем добавляемых файлов должен быть положительным числом")


if __name__ == "__main__":
    doctest.testmod()


