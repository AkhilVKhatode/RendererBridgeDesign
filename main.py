# Renderer.py - Interface for rendering methods
from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass
    
    @abstractmethod
    def render_rectangle(self, width, height):
        pass

# RasterRenderer.py - Concrete implementation for Raster Rendering
class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Raster Rendering: Drawing Circle with radius {radius}")
    
    def render_rectangle(self, width, height):
        print(f"Raster Rendering: Drawing Rectangle with width {width} and height {height}")

# VectorRenderer.py - Concrete implementation for Vector Rendering
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Vector Rendering: Drawing Circle with radius {radius}")
    
    def render_rectangle(self, width, height):
        print(f"Vector Rendering: Drawing Rectangle with width {width} and height {height}")

# Shape.py - Abstract class for shapes
class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self):
        pass

# Circle.py - Refined abstraction for Circle
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius
    
    def draw(self):
        self.renderer.render_circle(self.radius)

# Rectangle.py - Refined abstraction for Rectangle
class Rectangle(Shape):
    def __init__(self, renderer, width, height):
        super().__init__(renderer)
        self.width = width
        self.height = height
    
    def draw(self):
        self.renderer.render_rectangle(self.width, self.height)

# DrawingApp.py
def main():
    raster_renderer = RasterRenderer()
    vector_renderer = VectorRenderer()
    
    raster_circle = Circle(raster_renderer, 5)
    vector_circle = Circle(vector_renderer, 5)
    raster_rectangle = Rectangle(raster_renderer, 10, 5)
    vector_rectangle = Rectangle(vector_renderer, 10, 5)
    
    raster_circle.draw()
    vector_circle.draw()
    raster_rectangle.draw()
    vector_rectangle.draw()

if __name__ == "__main__":
    main()
