"""The prototype or clone pattern provides a mechanism to copy or clone complex
objects instead of re-creating them from scratch. It delegates the task of cloning to
the object itself which implements a `clone` method. Thus, we decouple the code
from the object."""
import copy


class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color})"

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    original_rectangle = Rectangle(30, 40, "blue")
    print("Original:", original_rectangle)

    cloned_rectangle = original_rectangle.clone()
    print("Cloned", cloned_rectangle)
