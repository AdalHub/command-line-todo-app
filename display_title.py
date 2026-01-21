from colorama import init, Fore, Style
import sys

# Initialize colorama for cross-platform support
init(autoreset=True)

def display_rainbow_title():
    """Display TO-DO-Y title in ASCII art with rainbow colors"""
    
    # ASCII art for TO-DO-Y
    ascii_art = [
"___________                  .___                       ",
"\__    ___/___             __| _/____            ___.__.",
"  |    | /  _ \   ______  / __ |/  _ \   ______ <   |  |",
"  |    |(  (_) ) /_____/ / /_/ (  (_) ) /_____/  \___  |",
"  |____| \____/          \____ |\____/           / ____|",
"                              \/                 \/     ",
    ]
    
    gradient_colors = [
        '\033[38;5;27m',   # Deep blue
        '\033[38;5;33m',   # Medium blue
        '\033[38;5;39m',   # Light blue
        '\033[38;5;45m',   # Cyan-blue
        '\033[38;5;51m',   # Bright cyan
        '\033[38;5;87m',   # Sky blue
        '\033[38;5;123m',  # Light cyan
        '\033[38;5;159m',  # Pale cyan
        '\033[38;5;195m',  # Very pale cyan
        '\033[38;5;219m',  # Light pink
        '\033[38;5;213m',  # Pink
        '\033[38;5;207m',  # Bright pink
        '\033[38;5;201m',  # Hot pink
        '\033[38;5;200m',  # Deep pink
        '\033[38;5;199m',  # Magenta pink
    ]
    
    print("\n")
    
    # Print each line with gradient color
    for i, line in enumerate(ascii_art):
        color = gradient_colors[i % len(gradient_colors)]
        print(color + line)
    
    print(Style.RESET_ALL)
    print("\n")
