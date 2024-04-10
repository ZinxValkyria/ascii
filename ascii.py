def print_ascii_art():
    sword_ascii = r'''
        _
       /|
      /_|                  _________
        |                 ///// \\\\\
        |                /////   \\\\\
TTTTTTTTTTTTTTTT        /////0   0\\\\\    
                        \\\\\  ^  /////
                         \\\\\ - /////
                           

'''
    print(sword_ascii)

print_ascii_art()

import random
import time

def print_matrix(rows, cols):
    symbols = "01"  # Define symbols for the matrix (you can customize this if needed)
    green_color = "\033[32m"  # ANSI escape code for green color
    reset_color = "\033[0m"   # ANSI escape code to reset color
    while True:
        for _ in range(rows):
            row = ''.join(random.choice(symbols) for _ in range(cols))
            print(green_color + row + reset_color)  # Print in green color
        time.sleep(0.1)  # Add a small delay for effect
        print("\033[H\033[J")  # Clear the screen (works on Unix-like systems, adjust as needed)

# Adjust rows and cols for the size of the matrix
print_matrix(25, 100)




