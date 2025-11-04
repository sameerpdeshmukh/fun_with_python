from practice_1 import Circle

print("Execution happens from top down even if there is main function defined")

def main():
    print("I am in to main function")
    circle = Circle(7)
    area = circle.calculate_area()
    print(f"The area of the circle is: {area}")

if __name__ == "__main__":
    main()

# Output:
# Execution happens from top down even if there is main function defined
# I am in to main function
# I am in __init__ method 7
# self refers to the current instance of the class: <practice_1.Circle object at 0x000002073608BA10>
# Radius has been set to: 7
# The area of the circle is: 153.93804002589985
