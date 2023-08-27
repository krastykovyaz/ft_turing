import sys
from validation import Validator
from printing import Printer
from computing import Mover

def ft_turing():
    data, inpt = validator.check_keys()
    printer = Printer(data)
    printer.draw()
    mover = Mover()
    mover.compute_state()


if __name__=='__main__':
    if (len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h")):
        print(
            "usage: ft_turing [-h] jsonfile input\n\npositional arguments:\n\tjsonfile\tjson description of the machine\n\n\tinput\t\tinput of the machine\n\noptional arguments:\n\t-h, --help\tshow this help message and exit")
        sys.exit(0)
    validator = Validator(sys.argv)
    print(ft_turing())
