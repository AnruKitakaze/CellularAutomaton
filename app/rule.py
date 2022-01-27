class Rule:
    """
    Правила для одномерного двухцветного клеточного автомата
    """
    _rule: int = None

    def __init__(self, rule: int):
        if 0 <= rule <= 255:
            self._rule = rule
        else:
            raise ValueError

    def get_rule(self):
        return self._rule

    def set_rule(self, rule: int):
        if 0 <= rule <= 255:
            self._rule = rule
        else:
            raise ValueError
