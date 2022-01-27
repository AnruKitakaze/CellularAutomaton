from copy import copy


class Field:
    """
    Поле для одномерного двухцветного клеточного автомата
    """
    _field: list = None

    def __init__(self, size: int):
        self._field = [0 if position != size // 2 else 1 for position in range(size)]

    # TODO: Сюда бы проверку на входящие значения
    def set(self, field: list):
        self._field = copy(field)

    def get(self):
        return self._field
