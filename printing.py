class Printer:
    def __init__(self, data):
        self.data = data
        self.draw()

    def draw(self):
        print("*" * 80)
        print("*" + " " * 78 + "*")
        print("*{:^78}*".format(self.data["name"]))
        print("*" + " " * 78 + "*")
        print("*" * 80)
        print("Alphabet : " + str(self.data["alphabet"]).replace("'", "").replace("[", "[ ").replace("]", " ]"))
        print("States : " + str(self.data["states"]).replace("'", "").replace("[", "[ ").replace("]", " ]"))
        print("Initial : " + self.data["initial"])
        print("Finals : " + str(self.data["finals"]).replace("'", "").replace("[", "[ ").replace("]", " ]"))
        for state in self.data["states"]:
            if state not in self.data["finals"]:
                for step in self.data["transitions"][state]:
                    print(f"({state}, {step['read']}) -> ({step['to_state']}, {step['write']}, {step['action']})")
        print("*" * 80)