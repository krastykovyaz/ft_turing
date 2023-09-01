'''module for algorithm'''

class Mover:
    '''
        action class
    '''
    def __init__(self, data, inpt, mode):
        self.data = data
        self.inpt = inpt
        self.tape = list(inpt)
        self.mode = mode
        self.head = 10
        for _ in range(self.head):
            self.tape.insert(0, data["blank"])
        while (len(self.tape) < 1000):
            self.tape.append(data["blank"])
        self.state = data["initial"]
        self.bkp = []
        self.steps = 0


    def compute_state(self)->None:
        """
        calculate by the condition in the json
        """
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
            if self.mode == "print":
                print(f"[{''.join(print_tape)}] ({self.state}, {self.head - 10}:{self.tape[self.head]}) -> ", end="")
            check = next((x for x in self.data["transitions"][self.state] if x["read"] == self.tape[self.head]), None)
            if check is None:
                print("No transition for state and char")
                return -1
            if self.mode == "print":
                print(f"({check['to_state']}, {check['write']}, {check['action']})")
            self.tape[self.head] = check["write"]
            if check["action"] == "RIGHT":
                self.head += 1
            elif check["action"] == "LEFT":
                self.head -= 1
            self.state = check["to_state"]
        # return 0

    def computing(self)->int:
        """
        get steps in the blank
        """
        self.compute_state()
        while (self.tape[0] == self.data["blank"] and len(self.tape) > 1):
            self.tape.pop(0)
        while (self.tape[-1] == self.data["blank"] and len(self.tape) > 1):
            self.tape.pop()
        if self.mode == "print":
            print(f"[{''.join(self.tape)}] in {self.steps} steps")
        if (self.mode == "sample"):
            return self.steps
        return 0
