def add_color(message, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'orange': '\x1b[38;2;255;165;0m',
    }

    if color not in colors:
        raise ValueError("Invalid color specified. Available colors are: red, green, yellow, blue, purple, cyan")
    
    return f"{colors[color]}{message}\033[0m"
    
def print_color(message, color, end='\n'):
    print(add_color(message, color), end=end)
    