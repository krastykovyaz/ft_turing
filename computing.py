from validation import Validator

class Mover:
    def __init__(self, data, inpt):
        self.data = data
        self.inpt = inpt
        self.tape = list(input)
        self.validator = Validator()
        self.head = 10
        for _ in range(self.head):
            self.tape.insert(0, data["blank"])
        while (len(self.tape) < 1000):
            self.tape.append(data["blank"])
        self.state = data["initial"]
        self.bkp = []
        self.steps = 0


    def compute_state(self):
        while self.state not in self.data["finals"]:
            self.steps += 1
            print_tape = list(self.tape)
            print_tape.insert(self.head, "<")
            print_tape.insert(self.head + 2, ">")
            if ("".join(print_tape) + self.state) in self.bkp or self.head < 9:
                print("Infinite loop !")
                return -1
            self.bkp.append("".join(print_tape) + self.state)
            while (len(print_tape) > self.head + 12):
                print_tape.pop()
            for _ in range(self.head - 9):
                print_tape.pop(0)
            if self.validator.mode == "print":
                print(f"[{''.join(print_tape)}] ({self.state}, {self.head - 10}:{self.tape[self.head]}) -> ", end="")

            check = next((x for x in self.data["transitions"][self.state] if x["read"] == self.tape[self.head]), None)
            if check is None:
                print("No transition for this state and this char")
                return -1
            if self.validator.mode == "print":
                print(f"({check['to_state']}, {check['write']}, {check['action']})")
            self.tape[self.head] = check["write"]
            if check["action"] == "RIGHT":
                self.head += 1
            elif check["action"] == "LEFT":
                self.head -= 1
            self.state = check["to_state"]
            return 0

    def computing(self):
        if self.compute_state() == -1:
            return -1
        while (self.tape[0] == self.data["blank"] and len(self.tape) > 1):
            self.tape.pop(0)
        while (self.tape[-1] == self.data["blank"] and len(self.tape) > 1):
            self.tape.pop()
        if self.validator.mode == "print":
            print("[{}] in {} steps".format("".join(self.tape), self.steps))
        if (self.validator.mode == "sample"):
            return self.steps
        return 0
