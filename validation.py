import sys
import json
import settings as config

class Validator:
    def __init__(self, arguments, mode = "print"):
        self.args = arguments
        with open("./" + self.args[1], 'r') as jf:
            self.data = json.load(jf)
        self.input = self.args[2]
        self.mode = mode


    def check_keys(self):
        self.check_input()
        try:
            assert len(self.data.keys()) == len(config.JSON_KEYS) , "unknown key"
            for key in self.data.keys():
                assert key in self.data, f"{key} missed"
                if key in ["alphabet", "states", "transitions"]:
                    self.input = self.fill_input(key, self.input)
                if key == "finals":
                    for state in self.data[key]:
                        assert state in self.data["states"], "final state is not in states"
                if key == "states":
                    for state in self.data[key]:
                        if state in self.data["finals"]:
                            assert state not in self.data["transitions"], "final state must not be in transitions"
                            continue
                        assert state in self.data["transitions"], "transitions for a state missed"
                if key == "transitions":
                    for state in self.data[key]:
                        assert state in self.data["states"], "state is not in states"
                if key == "blank":
                    assert self.data[key] in self.data["alphabet"], "blank must be in alphabet"
                    assert self.data[key] not in input, "blank must not be in input"
            for char in self.input:
                assert char in self.data["alphabet"], "input must be in alphabet"
        except AssertionError as error:
            if self.mode == "print":
                print("Error: " + error.__str__())
            return -1
        except Exception as error:
            if self.mode == "print":
                print("Error: " + error.__str__())
            return -1
        return self.data, self.input



    def check_input(self):
        try:
            assert len(self.argv) == 3, "Wrong number of arguments"
            assert isinstance(self.argv[1], str), "jsonfile must be a string"
            assert isinstance(self.argv[2], str), "input must be a string"
            assert len(self.argv[2]) > 0, "input must not be empty"
        except AssertionError as error:
            print("Error: " + error.__str__())
            sys.exit(0)

    def raise_error(self, st, end, param):
        try:
            assert st != -1, f"{param} set for value in input but no value"
            assert end != -1, f"{param} set for value in input but no value"
        except AssertionError as error:
            if self.mode == "print":
                print("Error: " + error.__str__())
            sys.exit(0)

    def fill_input(self, key, input):
        if type(self.data[key]) == str and f"<{key}>" == self.data[key]:
            start = input.find(f"<{key}=") + config.STATES_DICT[key]
            end = input.find(">", start)
            self.raise_error(start, end, key)
            self.data[key] = json.loads(input[start:end])
            input = input[:start - config.STATES_DICT[key]] + input[end + 1:]
        return input

    def check_steps(self, state):
        assert len(self.data["transitions"][state].keys()) == len(config.JSON_STATES), "unknown key in states"
        for key in self.data.keys():
            assert key in self.data, f"{key} missed in states"
            assert key["to_state"] in self.data["states"], "to_state is not in states"


