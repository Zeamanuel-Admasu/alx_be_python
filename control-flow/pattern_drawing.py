# control-flow/pattern_drawing.py

size = int(input("Enter the size of the pattern: "))
row = 0

while row < size:
    for _ in range(size):
        print("*")
    # print()
    row += 1
