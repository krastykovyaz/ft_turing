'''main module for starting the program'''
import sys
from validation import Validator
from printing import Printer
from computing import Mover

def ft_turing(argv1: str, argv2: str, mode='print')->int:
    '''
    function for sequence of moving
    '''
    validator = Validator(argv1, argv2, mode)
    data, inpt = validator.check_keys()
    Printer(data)
    mover = Mover(data, inpt, validator.mode)
    return mover.computing()


if __name__=='__main__':
    if (len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h")):
        print(
            "usage: ft_turing [-h] jsonfile input\n\npositional arguments:\n\tjsonfile\tjson description of the machine\n\n\tinput\t\tinput of the machine\n\noptional arguments:\n\t-h, --help\tshow this help message and exit")
        sys.exit(0)
    ft_turing(sys.argv[1], sys.argv[2])
