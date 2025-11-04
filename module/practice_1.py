"""This is to understand the basics"""
import math

class Circle:
    """
    A class representing a circle with methods to calculate its area."""
    # Object initialization method
    def __init__(self, radius):
        print("I am in __init__ method", radius)
        print("self refers to the current instance of the class:", self)
        self.radius = radius
        print("Radius has been set to:", self.radius)
        
    def calculate_area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

def abc() -> None:
    """A simple function to demonstrate function definition."""
    print("I am in abc() function")