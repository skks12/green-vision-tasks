def do_rectangles_overlap(L1, R1, L2, R2):
    # If one rectangle is to the left of the other
    if L1[0] > R2[0] or L2[0] > R1[0]:
        return False

    # If one rectangle is above the other
    if R1[1] > L2[1] or R2[1] > L1[1]:
        return False

    return True

# Input coordinates for the first rectangle
L1 = tuple(map(int, input("Enter the coordinates of the top-left corner of the first rectangle (L1_x L1_y): ").split()))
R1 = tuple(map(int, input("Enter the coordinates of the bottom-right corner of the first rectangle (R1_x R1_y): ").split()))

# Input coordinates for the second rectangle
L2 = tuple(map(int, input("Enter the coordinates of the top-left corner of the second rectangle (L2_x L2_y): ").split()))
R2 = tuple(map(int, input("Enter the coordinates of the bottom-right corner of the second rectangle (R2_x R2_y): ").split()))

# Check if the rectangles overlap
if do_rectangles_overlap(L1, R1, L2, R2):
    print("The rectangles overlap.")
else:
    print("The rectangles do not overlap.")
