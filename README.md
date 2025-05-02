# Bridge Design Pattern: Shape Rendering Example

This repository demonstrates the implementation of the **Bridge Design Pattern** using Python. The Bridge pattern is a structural design pattern that decouples abstraction from its implementation, allowing both to vary independently.

## Overview

In this example, the `Shape` class serves as an abstraction, and the `Renderer` interface defines how the shapes are rendered. The concrete implementations of the `Renderer` interface, `RasterRenderer` and `VectorRenderer`, handle the actual rendering of shapes in different ways. The shapes, `Circle` and `Rectangle`, utilize the renderer to draw themselves.

## Design Pattern

The **Bridge Pattern** is used to:
- **Decouple** abstraction (`Shape`) from implementation (`Renderer`).
- Allow **independent changes** to the abstraction and the implementation.

### Structure:
- `Renderer`: An interface that defines the methods for rendering shapes.
- `RasterRenderer` and `VectorRenderer`: Concrete implementations of `Renderer` for raster and vector-based rendering, respectively.
- `Shape`: Abstract class representing shapes. Subclasses are `Circle` and `Rectangle`.
- `Circle` and `Rectangle`: Concrete implementations of `Shape`, representing specific shapes.

## Classes

- `Renderer`: Contains the `Renderer` interface class.
- `RasterRenderer`: Implements the `Renderer` interface for raster rendering.
- `VectorRenderer`: Implements the `Renderer` interface for vector rendering.
- `Shape`: Contains the abstract `Shape` class.
- `Circle`: Implements the `Shape` class for circle.
- `Rectangle`: Implements the `Shape` class for rectangle.
- `DrawingApp`: Contains the `main()` function to demonstrate the usage of the bridge pattern by drawing shapes using different renderers.

## Example Output
```mathematica
Raster Rendering: Drawing Circle with radius 5
Vector Rendering: Drawing Circle with radius 5
Raster Rendering: Drawing Rectangle with width 10 and height 5
Vector Rendering: Drawing Rectangle with width 10 and height 5
```
