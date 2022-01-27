from rule import Rule
from field import Field


class CellularAutomaton:
    """
    Двухцветный одномерный клеточный автомат на замкнутом контуре
    """
    _rule: Rule = None
    _field: Field = None
    state: list = None

    def __init__(self, rule: Rule, field: Field):
        self._rule = rule
        self._field = field

    def play(self, steps: int = 10) -> list:
        state = list()
        state.append(self._field.get())
        for j in range(steps):
            tmp = [0 for _ in range(len(self._field.get()))]

            for i in range(len(self._field.get())):
                tmp[i] = 1 if self.is_alive(
                    self._field.get()[i - 1] * 2 ** 2 +
                    self._field.get()[i] * 2 ** 1 +
                    self._field.get()[(i + 1) % len(self._field.get())] * 2 ** 0) \
                    else 0

            state.append(tmp)
            self._field.set(tmp)

        return state

    def set_field(self, field: Field):
        self._field = field

    def set_rule(self, rule):
        self._rule.set_rule(rule)

    def get_rule(self):
        self._rule.get_rule()

    def is_alive(self, bit: int) -> bool:
        """
        Возвращает значение истинности bit-ого разряда правила
        Быстрее, чем return self._rule & 2 ** bit != 0
        """
        return self._rule.get_rule() & 1 << bit != 0
