from colorama import init, Fore, Style
import sys
import os

# Initialize colorama for cross-platform support
init(autoreset=True)
# Get the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the full path to tasks.json
ASCII_FACE_FILE = os.path.join(SCRIPT_DIR, "ascii_face.txt")

def extract_face_ascii_art():
    """Extract the face ASCII art from the current script file."""
    ascii_art_face = []


    with open(ASCII_FACE_FILE, 'r') as file:
        for line in file:
            
            ascii_art_face.append(line.rstrip('\n'))
    
    return ascii_art_face


def display_rainbow_title():
    """Display TO-DO-Y title in ASCII art with rainbow colors"""
    
    # ASCII art for TO-DO-Y
    ascii_art = [
        r"___________                  .___                       ",
        r"\__    ___/___             __| _/____            ___.__.",
        r"  |    | /  _ \   ______  / __ |/  _ \   ______ <   |  |",
        r"  |    |(  (_) ) /_____/ / /_/ (  (_) ) /_____/  \___  |",
        r"  |____| \____/          \____ |\____/           / ____|",
        r"                              \/                 \/     ",
    ]


    title_width= max(len(line) for line in ascii_art)
    ascii_art_face_to_merge_with_title = extract_face_ascii_art()
    final_title_merged_side_by_side = []
    face_width = max(len(line) for line in ascii_art_face_to_merge_with_title)
    #total_width = title_width + face_width + 5  # 5 spaces between title and face
    for i in range(max(len(ascii_art), len(ascii_art_face_to_merge_with_title))):
        title_line = ascii_art[i] if i < len(ascii_art) else " " * title_width
        face_line = ascii_art_face_to_merge_with_title[i] if i < len(ascii_art_face_to_merge_with_title) else " " * face_width
        final_title_merged_side_by_side.append(title_line + "     " + face_line)


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
    for i, line in enumerate(final_title_merged_side_by_side):
        color = gradient_colors[i % len(gradient_colors)]
        print(color + line)
    
    print(Style.RESET_ALL)
    print("\n")
