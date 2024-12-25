import cv2
import numpy as np


# Function to draw polygons on the image
def draw_polygons(image, polygons, color=(0, 255, 0), thickness=2):
    """
    Draws polygons on the given image.

    :param image: Input image (numpy array)
    :param polygons: List of polygons, each polygon is a list of (x, y) tuples
    :param color: Color of the polygon lines
    :param thickness: Thickness of the polygon lines
    :return: Image with drawn polygons
    """
    for polygon in polygons:
        pts = np.array(polygon, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], isClosed=True, color=color, thickness=thickness)
    return image


# Test the function
def main():
    # Create a blank image
    width, height = 800, 600
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Define some test polygons
    polygons = [[(100, 100), (200, 100), (200, 200), (100, 200)],  # Square
        [(300, 300), (400, 350), (350, 450)],  # Triangle
        [(500, 100), (550, 150), (520, 200), (480, 150)],  # Diamond
    ]

    # Draw polygons on the image
    annotated_image = draw_polygons(image, polygons, color=(0, 255, 0), thickness=3)

    # Show the image with polygons
    cv2.imshow("Annotated Image", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Optionally save the annotated image
    # cv2.imwrite("annotated_image.png", annotated_image)


if __name__ == "__main__":
    main()
