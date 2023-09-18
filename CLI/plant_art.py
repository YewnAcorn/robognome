# Function to print ASCII art from a .txt file
def print_ascii_art(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            print(line, end='')  # end='' ensures that the newlines present in the file are preserved

# Usage
def print_bigTree():
    print_ascii_art('asciiplants/bigTree.ascii')


def print_halfTree():
    print_ascii_art('asciiplants/halfTree.ascii')


def print_miseltoe():
    print_ascii_art('asciiplants/miseltoe.ascii')


def print_weed():
    print_ascii_art('asciiplants/weed.ascii')


def print_heartTree():
    print_ascii_art('asciiplants/heartTree.ascii')


def print_twoPines():
    print_ascii_art('asciiplants/twoPines.ascii')

def print_FarmBrain():
    print_ascii_art('asciiplants/FarmBrain.ascii')

# art_list = [print_bigTree(), print_halfTree(), print_miseltoe(), print_weed(), print_heartTree(), print_twoPines(), print_FarmBrain.ascii]
