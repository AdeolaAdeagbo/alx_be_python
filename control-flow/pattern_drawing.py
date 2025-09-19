# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:
    # Print one row of asterisks
    for _ in range(size):
        print("*", end="")
    print()  # Move to next line
    row += 1
