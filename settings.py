import numpy as np

JSON_KEYS = ["name", "alphabet", "blank", "states", "initial", "finals", "transitions"]
JSON_STATES = ["read", "to_state", "write", "action"]
STATES_DICT = {"alphabet": 10, "states": 8, "transitions": 13}
COLOR_NOTATION = {"O(1)": lambda abscissa: [1 for _ in abscissa],
                  "O(logn)": lambda abscissa: [np.log(x) for x in abscissa],
                  "O(n^2)": lambda abscissa: [x * x for x in abscissa],
                    "O(n)":lambda abscissa: [x for x in abscissa],
                  "O(nlogn)": lambda abscissa: [x * np.log(x) for x in abscissa],
                  "O(n!)": lambda abscissa: [factorial(x) for x in abscissa],
                  "O(2^n)": lambda abscissa: [2**(x) for x in abscissa]}



def factorial(val):
    if val == 0 or val == 1:
        return 1
    return val * factorial(val - 1)
