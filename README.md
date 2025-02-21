# Hough Transform Circle Detector

## Overview
This project implements a Hough Transform-based circle detector to identify circles of a given radius in an input image. The implementation includes an edge detection function and a circle detection function, both of which avoid using built-in Python functions for finding edges or circles.

## Features
- **Edge Detection:** Computes edges in an image using gradient magnitude and orientation.
- **Circle Detection:** Uses the Hough Transform method to identify potential circle centers based on edge orientation.
- **Visualization:** Detected circles are displayed on the original image.


## Usage
### Edge Detection
```python
edges = detect_edges(img, threshold)
```
- `img`: Input RGB image (uint8).
- `threshold`: User-defined threshold for detecting edges.
- Returns `edges`: An Nx4 matrix containing x, y locations, gradient magnitude, and orientation.

### Circle Detection
```python
centers = detect_circles(img, edges, radius, top_k)
```
- `img`: Input image.
- `edges`: Detected edges from `detect_edges`.
- `radius`: Approximate radius of circles to detect.
- `top_k`: Number of top circle candidates to visualize.
- Returns `centers`: Nx2 matrix with x, y positions of detected circles.




