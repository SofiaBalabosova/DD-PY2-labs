class Book:

    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self) -> str:
        return self.__name

    @property
    def author(self) -> str:
        return self.__author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        return self._duration
    
    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, (float, int)):
            raise TypeError("Длительность аудиокниги должна быть int или float")
        if new_duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным числом")
        self._duration = new_duration
