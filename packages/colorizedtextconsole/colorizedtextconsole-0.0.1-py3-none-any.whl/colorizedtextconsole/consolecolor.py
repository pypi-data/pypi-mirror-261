from enum import Enum

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ConsoleColor(Enum):
    Blue = bcolors.OKBLUE
    Cyan = bcolors.OKCYAN
    Green = bcolors.OKGREEN
    Warning = bcolors.WARNING
    Fail = bcolors.FAIL

def colorized(text: str, consoleColor: ConsoleColor = None, bold: bool = False, underline: bool = False):
    # Determine underline tag
    underlineTag = bcolors.UNDERLINE if underline else ''

    # Determine bold tag
    boldTag = bcolors.BOLD if bold else ''

    # Determine color tag
    colorTag = '' if consoleColor is None else consoleColor.value

    return f"{underlineTag}{boldTag}{colorTag}{text}{bcolors.ENDC}"