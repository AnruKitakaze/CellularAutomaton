from matplotlib import pyplot as plt

from cellular_automaton import CellularAutomaton
from field import Field
from rule import Rule


def main():
    x = 20
    size = x * 2 + 1
    field = Field(0)
    rule = Rule(30)

    automaton = CellularAutomaton(rule, field)
    state = automaton.play(20)

    plt.imshow(state)
    plt.show()


if __name__ == '__main__':
    main()
